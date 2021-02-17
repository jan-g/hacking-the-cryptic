def display(g):
    for y in range(g.height):
        for x in range(g.width):
            digit, snake = g(x, y)
            if snake:
                print("[{}]".format(digit), end="")
            else:
                print(" {} ".format(digit), end="")
            if x % 3 == 2:
                print(" ", end="")
        print()
        if y % 3 == 2:
            print()


