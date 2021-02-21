from z3 import Solver, And, Not, sat, Z3Exception


class Grid:
    SOLVER = Solver

    def __init__(self, grid, **aux):
        grid = [l for line in grid if (l := line.replace(" ", "")) != ""]

        self.width = len(grid[0])
        self.height = len(grid)
        self.cell = {}
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                self.cell[x, y] = char

        for kw in aux:
            setattr(self, kw, aux[kw])

        self.solver = self.SOLVER()
        self.model = None
        self.vars = {}
        self.setup_vars()

    def coords(self):
        for y in range(self.height):
            for x in range(self.width):
                yield x, y

    def setup_vars(self):
        raise NotImplementedError()

    def __setitem__(self, item, value):
        self.vars[item] = value

    def __getitem__(self, item):
        return self.vars[item]

    def add(self, constraint):
        self.solver.add(constraint)

    def solve(self):
        if self.model is not None:
            assignments = []
            for _, var in self.vars.items():
                assignments.append(var == self.eval(var))
            self.add(Not(And(*assignments)))
        if self.solver.check() == sat:
            self.model = self.solver.model()
            return True
        return False

    def eval(self, var, cast=None):
        result = self.model.eval(var)
        if cast is not None:
            try:
                result = cast(result)
            except (TypeError, Z3Exception):
                result = None
        return result

    def __call__(self, x, y):
        raise NotImplementedError()
