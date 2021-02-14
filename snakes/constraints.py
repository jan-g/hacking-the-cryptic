from z3 import Not, And, Or, If, Implies


def constrain(g):
    place_head(g)
    place_tail(g)
    head_and_tail_distinct(g)
    head_distances(g)
    tail_distances(g)
    head_is_a_snake(g)


def Abs(x):
    return If(x < 0, -x, x)


def Manh(x1, y1, x2, y2):
    return Abs(x1 - x2) + Abs(y1 - y2)


def place_endpoint(g, ex, ey):
    # The endpoint must be on the grid
    g.add(0 <= ex)
    g.add(ex < g.width)
    g.add(0 <= ey)
    g.add(ey < g.height)

    # The endpoint must not be on a marked cell
    for y in range(g.height):
        for x in range(g.width):
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
    for y in range(g.height):
        for x in range(g.width):
            c = marker(x, y)
            if c is not None:
                g.add(c == Manh(x, y, ex, ey))


def head_distances(g):
    endpoint_distances(g, *g.head(), g.head_mark)


def tail_distances(g):
    endpoint_distances(g, *g.tail(), g.tail_mark)


def head_is_a_snake(g):
    hx, hy = g.head()
    for y in range(g.height):
        for x in range(g.width):
            c = g.snake(x, y)
            if c is not None:
                # For the moment, this will leave some snake variables unbound
                # g.add(Implies(And(hx == x, hy == y), c))
                g.add(And(hx == x, hy == y) == c)
