from collections import namedtuple
from z3 import Solver, Int, sat


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
        self.solver = Solver()
        self.model = None

        # Set up variables
        self.vars = {}

        # Head location
        self["hx"] = Int("hx")
        self["hy"] = Int("hy")

    def __setitem__(self, item, var):
        if item in self.vars:
            raise Exception("can't insert a variable twice")
        self.vars[item] = var

    def __getitem__(self, item):
        return self.vars[item]

    def __call__(self, x, y):
        c = self.grid[x, y]
        if c == ".":
            if x == self.eval(self["hx"]) and y == self.eval(self["hy"]):
                return Head()
            return Empty()
        elif c == "H":
            return HeadMark(0)
        elif c == "T":
            return TailMark(0)
        else:
            raise ValueError("unknown value at {}, {}".format(x, y))

    def solve(self):
        if self.solver.check() != sat:
            return False
        self.model = self.solver.model()
        return True

    def eval(self, var):
        return self.model.eval(var)

    def add(self, constraint):
        """Add a constraint to be satisfied"""
        self.solver.add(constraint)

    def head(self):
        return self["hx"], self["hy"]
