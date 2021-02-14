from collections import namedtuple

Empty = namedtuple("Empty", [])
HeadMark = namedtuple("HeadMark", ["distance"])
TailMark = namedtuple("TailMark", ["distance"])
Snake = namedtuple("Snake", [])
Head = namedtuple("Head", [])
Tail = namedtuple("Tail", [])


class Grid:
    def __init__(self, lines):
        self.grid = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self.grid[x, y] = char
        self.height = len(lines)
        self.width = len(lines[0])

    def __call__(self, x, y):
        c = self.grid[x, y]
        if c == ".":
            return Empty()
        elif c == "H":
            return HeadMark(0)
        elif c == "T":
            return TailMark(0)
        else:
            raise ValueError("unknown value at {}, {}".format(x, y))

    def solve(self):
        return False
