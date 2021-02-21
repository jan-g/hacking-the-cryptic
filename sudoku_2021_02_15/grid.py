from z3 import Int, Bool
from grid import Grid as BaseGrid


class Grid(BaseGrid):
    def setup_vars(self):
        for x, y in self.coords():
            self["digit_{}_{}".format(x, y)] = Int("digit_{}_{}".format(x, y))
            self["snake_{}_{}".format(x, y)] = Bool("snake_{}_{}".format(x, y))

    def __call__(self, x, y):
        return self.eval(self.digit(x, y), lambda v: v.as_long()), self.eval(self.snake(x, y), bool)

    def digit(self, x, y):
        return self["digit_{}_{}".format(x, y)]

    def snake(self, x, y):
        return self["snake_{}_{}".format(x, y)]
