def constrain(g):
    place_head(g)


def place_head(g):
    hx, hy = g.head()
    g.add(0 <= hx)
    g.add(hx < g.width)
    g.add(0 <= hy)
    g.add(hy < g.height)

