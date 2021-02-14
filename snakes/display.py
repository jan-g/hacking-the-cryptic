from .grid import Empty, Head, Tail, Snake, HeadMark, TailMark


def display(g):
    for y in range(g.height):
        for x in range(g.width):
            c = g(x, y)
            if isinstance(c, Empty):
                print(". ", end="")
            elif isinstance(c, HeadMark):
                print("h{}".format(c.distance), end="")
            elif isinstance(c, TailMark):
                print("t{}".format(c.distance), end="")
            elif isinstance(c, Head):
                print("HH", end="")
            elif isinstance(c, Tail):
                print("TT", end="")
            elif isinstance(c, Snake):
                print("**", end="")
            else:
                print("??", end="")
        print()
    print()

