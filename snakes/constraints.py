from z3 import Not, And, Or


def constrain(g):
    place_head(g)


def place_head(g):
    # The head must be on the grid
    hx, hy = g.head()
    g.add(0 <= hx)
    g.add(hx < g.width)
    g.add(0 <= hy)
    g.add(hy < g.height)

    # The head must not be on a marked cell
    for y in range(g.height):
        for x in range(g.width):
            if g.snake_possible(x, y):
                continue
            # The head can't be here.
            g.add(Or(hx != x, hy != y))
