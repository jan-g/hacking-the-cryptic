from z3 import Not, And, Or, If, Implies
from z3 import Function, IntSort, BoolSort, TransitiveClosure
from z3 import Datatype


def constrain(g):
    place_head(g)
    place_tail(g)
    head_and_tail_distinct(g)
    head_distances(g)
    tail_distances(g)
    head_is_a_snake(g)
    tail_is_a_snake(g)
    snakes_are_connected(g)
    snakes_find_the_head(g)


def Abs(x):
    return If(x < 0, -x, x)


def Manh(x1, y1, x2, y2):
    return Abs(x1 - x2) + Abs(y1 - y2)


def manh(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def BoolToInt(x):
    return If(x, 1, 0)


def place_endpoint(g, ex, ey):
    # The endpoint must be on the grid
    g.add(0 <= ex)
    g.add(ex < g.width)
    g.add(0 <= ey)
    g.add(ey < g.height)

    # The endpoint must not be on a marked cell
    for x, y in g.coords():
        if g.snake_possible(x, y):
            continue
        # The endpoint can't be here.
        g.add(Or(ex != x, ey != y))


def place_head(g):
    place_endpoint(g, *g.head())


def place_tail(g):
    place_endpoint(g, *g.tail())


def head_and_tail_distinct(g):
    hx, hy = g.head()
    tx, ty = g.tail()
    g.add(Manh(hx, hy, tx, ty) > 1)


def endpoint_distances(g, ex, ey, marker):
    for x, y in g.coords():
        c = marker(x, y)
        if c is not None:
            g.add(c == Manh(x, y, ex, ey))


def head_distances(g):
    endpoint_distances(g, *g.head(), g.head_mark)


def tail_distances(g):
    endpoint_distances(g, *g.tail(), g.tail_mark)


def endpoint_is_a_snake(g, ex, ey):
    for x, y in g.coords():
        c = g.snake(x, y)
        if c is not None:
            # For the moment, this will leave some snake variables unbound
            g.add(Implies(And(ex == x, ey == y), c))


def head_is_a_snake(g):
    endpoint_is_a_snake(g, *g.head())


def tail_is_a_snake(g):
    endpoint_is_a_snake(g, *g.tail())


def snakes_are_connected(g):
    hx, hy = g.head()
    tx, ty = g.tail()

    for x, y in g.coords():
        c = g.snake(x, y)
        if c is None:
            continue
        ns = g.orthogonal_neighbours(x, y)

        # If this cell has a snake in it, then it must have exactly two neighbours that are snakes -
        # or, it must be an endpoint, in which case it has one neighbour.

        is_head = And(x == hx, y == hy)
        is_tail = And(x == tx, y == ty)
        is_endpoint = Or(is_head, is_tail)

        snake_neighbours = sum(BoolToInt(ns[c2]) for c2 in ns)
        g.add(Implies(c, snake_neighbours == If(is_endpoint, 1, 2)))


def snakes_find_the_head(g):
    # We'll want a type that represents a cell in the grid. We use a datatype because we can make it a sum type -
    # that is, its 0-arity constructors represent a closed enumeration of distinct objects.
    Cell = Datatype("Cell")

    for x, y in g.coords():
        if g.snake(x, y) is not None:
            Cell.declare("cell_{}_{}".format(x, y))
    Cell = Cell.create()

    # We'll have two functions that we explicitly declare. One is the short-distance "connected" relationship.
    # The other is a convenience function for turning the coordinates of a cell into the datatype member that
    # represents that position.
    Connected = Function("Connected", Cell, Cell, BoolSort())
    XYToCell = Function("XYToCell", IntSort(), IntSort(), Cell)

    cell = {}
    for x, y in g.coords():
        if g.snake(x, y) is not None:
            cell[x, y] = getattr(Cell, "cell_{}_{}".format(x, y))
            g.add(XYToCell(x, y) == cell[x, y])

    # Two cells are connected *if and only* if they are adjacent and both hold snakes
    # We need to be really clear about the "and only if" part; a naive implementation here will let the
    # solver fill in other arbitrary values for `Connected` in order to make the desired outcome true.
    # We do this by ensuring there's a value declared for our Connected relationship between every pair
    # of potential arguments.

    for x1, y1 in g.coords():
        c1 = g.snake(x1, y1)
        if c1 is None:
            continue
        # If there's a snake here, the cell is connected to itself
        g.add(Connected(cell[x1, y1], cell[x1, y1]) == c1)
        for x2, y2 in g.coords():
            c2 = g.snake(x2, y2)
            if c2 is None or (x1, y1) == (x2, y2):
                continue
            if manh(x1, y1, x2, y2) == 1:
                g.add(Connected(cell[x1, y1], cell[x2, y2]) == And(c1, c2))
            else:
                # Without this, our function declaration is only partial. The solver can fill in missing values
                # in order to scupper our good intentions.
                g.add(Not(Connected(cell[x1, y1], cell[x2, y2])))

    # The transitive closure of Connectedness is Reaches
    Reaches = TransitiveClosure(Connected)

    # For every cell in the grid, if it's a snake then we can connect it to the head position
    hx, hy = g.head()
    for x, y in g.coords():
        c = g.snake(x, y)
        if c is None:
            continue

        g.add(Implies(c, Reaches(cell[x, y], XYToCell(hx, hy))))
