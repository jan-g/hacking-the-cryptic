from z3 import Distinct, Datatype, Function, BoolSort, IntSort, Not, And, Implies, TransitiveClosure, If, Or


def constrain(g):
    digits_1_to_9(g)
    head_and_tail(g)
    snake_orthogonally_connected(g)
    snake_doesnt_touch_itself(g)
    snake(g)
    rows_distinct(g)
    columns_distinct(g)
    boxes_distinct(g)
    snake_sums(g)


def digits_1_to_9(g):
    for x, y in g.coords():
        digit = g.digit(x, y)
        g.add(1 <= digit)
        g.add(digit <= 9)


def rows_distinct(g):
    for y in range(g.height):
        g.add(Distinct(*(g.digit(x, y) for x in range(g.width))))


def columns_distinct(g):
    for x in range(g.width):
        g.add(Distinct(*(g.digit(x, y) for y in range(g.height))))


def boxes_distinct(g):
    dx = dy = 3
    for j in range(g.height // dy):
        for i in range(g.width // dx):
            g.add(Distinct(*(g.digit(x + i * dx, y + j * dy) for y in range(dy) for x in range(dx))))


def head_and_tail(g):
    g.add(g.snake(*g.head))
    g.add(g.snake(*g.tail))


def manh(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def snake(g):
    Cell = Datatype("Cell")

    for x, y in g.coords():
        if g.snake(x, y) is not None:
            Cell.declare("cell_{}_{}".format(x, y))
    Cell = Cell.create()

    # We'll have two functions that we explicitly declare. One is the short-distance "connected" relationship.
    # The other is a convenience function for turning the coordinates of a cell into the datatype member that
    # represents that position.
    Connected = Function("Connected", Cell, Cell, BoolSort())

    cell = {}
    for x, y in g.coords():
        if g.snake(x, y) is not None:
            cell[x, y] = getattr(Cell, "cell_{}_{}".format(x, y))

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
    hx, hy = g.head
    for x, y in g.coords():
        c = g.snake(x, y)
        if c is None:
            continue

        g.add(Implies(c, Reaches(cell[x, y], cell[hx, hy])))


def snake_sums(g):
    for y in range(g.height):
        row = sum(If(g.snake(x, y), g.digit(x, y), 0) for x in range(g.width))
        g.add(row == g.rows[y])

    for x in range(g.width):
        row = sum(If(g.snake(x, y), g.digit(x, y), 0) for y in range(g.height))
        g.add(row == g.columns[x])


def orthogonal(g, x, y):
    for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        x2, y2 = x + dx, y + dy
        if 0 <= x2 < g.width and 0 <= y2 < g.height:
            yield x2, y2


def surrounding(g, x, y):
    for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        x2, y2 = x + dx, y + dy
        if 0 <= x2 < g.width and 0 <= y2 < g.height:
            yield x2, y2


def BoolToInt(x):
    return If(x, 1, 0)


def snake_orthogonally_connected(g):
    # Orthogonally, we don't branch
    for x, y in g.coords():
        c = g.snake(x, y)
        number_surrounding = sum(BoolToInt(g.snake(x2, y2)) for x2, y2 in orthogonal(g, x, y))
        is_head = (x, y) == g.head
        is_tail = (x, y) == g.tail
        is_endpoint = Or(is_head, is_tail)
        g.add(Implies(c, number_surrounding == If(is_endpoint, 1, 2)))


def snake_doesnt_touch_itself(g):
    for x, y in g.coords():
        c = g.snake(x, y)
        for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
            x2, y2 = x + dx, y + dy
            if not(0 <= x2 < g.width and 0 <= y2 < g.height):
                continue
            c_corner = g.snake(x2, y2)

            # The two squares immediately connecting the corner and the centre
            c1 = g.snake(x2, y)
            c2 = g.snake(x, y2)

            # If the centre square is on and the corner square is on, that implies that one of their conencting squares must be on
            g.add(Implies(And(c, c_corner), Or(c1, c2)))
