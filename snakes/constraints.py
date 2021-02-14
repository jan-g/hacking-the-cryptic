from z3 import Not, And, Or


def constrain(g):
    place_head(g)
    place_tail(g)


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


