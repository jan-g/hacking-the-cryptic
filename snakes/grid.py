from collections import namedtuple
from z3 import Solver, Int, sat, Not, And


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

        # Tail location
        self["tx"] = Int("tx")
        self["ty"] = Int("ty")

        # Cells with a head marker
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[x, y] == "H":
                    v = "head_{}_{}".format(x, y)
                    self[v] = Int(v)

                if self.grid[x, y] == "T":
                    v = "tail_{}_{}".format(x, y)
                    self[v] = Int(v)

    def __setitem__(self, item, var):
        if item in self.vars:
            raise Exception("can't insert a variable twice")
        self.vars[item] = var

    def __getitem__(self, item):
        return self.vars[item]

    def __call__(self, x, y):
        c = self.grid[x, y]
        if c == ".":
            hx, hy = self.head()
            if x == self.eval(hx) and y == self.eval(hy):
                return Head()
            tx, ty = self.tail()
            if x == self.eval(tx) and y == self.eval(ty):
                return Tail()
            return Empty()
        elif c == "H":
            return HeadMark(self.eval(self["head_{}_{}".format(x, y)]))
        elif c == "T":
            return TailMark(self.eval(self["tail_{}_{}".format(x, y)]))
        else:
            raise ValueError("unknown value at {}, {}".format(x, y))

    def solve(self):
        """Find a first or next solution"""
        if self.model is not None:
            # We hae a potential solution. Collect up the values assigned to each variable in it
            # This gives us, eg, [hx == 0, hy == 0]
            assignments = [var == self.eval(var) for (_, var) in self.vars.items()]

            # Now, add the negation of the conjunction of these. In other words, explicitly rule out
            # this particular solution
            self.add(Not(And(*assignments)))

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

    def tail(self):
        return self["tx"], self["ty"]

    def snake_possible(self, x, y):
        return self.grid[x, y] == "."

    def head_mark(self, x, y):
        if self.grid[x, y] == "H":
            return self["head_{}_{}".format(x, y)]
        return None

    def tail_mark(self, x, y):
        if self.grid[x, y] == "T":
            return self["tail_{}_{}".format(x, y)]
        return None
