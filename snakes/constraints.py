from z3 import Not, And, Or, If


def constrain(g):
    place_head(g)
    place_tail(g)
    head_and_tail_distinct(g)


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
