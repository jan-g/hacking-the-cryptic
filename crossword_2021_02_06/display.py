def display(g):
    for y in range(g.height):
        for x in range(g.width):
            c = g(x, y)
            if c is None:
                c = "?"
            if c == "#":
                c = " "
            print(c, end="")
        print()
    print()

    print("words not placed:", "".join(word for word in g.words if not g.is_placed(word)))
    print()
