from string import ascii_uppercase
from z3 import Int, Bool, Optimize

from grid import Grid as BaseGrid


def cell(x, y):
    return "char_{}_{}".format(x, y)


def int_to_char(n):
    # It's okay for this to throw: Grid.eval(_, int_to_char) will catch and deal with that
    return ("?" + ascii_uppercase)[n.as_long()]


def char_to_int(c):
    assert c.isalpha()
    return ord(c.lower()) - ord('a') + 1


def strip(w):
    return w.lower().replace(" ", "").replace("-", "")


def placed(w):
    return "placed_{}".format(strip(w))


class Grid(BaseGrid):
    SOLVER = Optimize

    def setup_vars(self):
        for x, y in self.coords():
            if self.cell[x, y] == ".":
                self[cell(x, y)] = Int(cell(x, y))

        for w in self.words:
            self[placed(w)] = Bool(placed(w))

    def letter(self, x, y):
        if self.cell.get((x, y)) == ".":
            return self[cell(x, y)]
        return None

    def placed(self, w):
        return self[placed(w)]

    def __call__(self, x, y):
        if (c := self.letter(x, y)) is not None:
            return self.eval(c, int_to_char)
        else:
            return self.cell[x, y]

    def is_placed(self, w):
        return self.eval(self.placed(w), bool)
