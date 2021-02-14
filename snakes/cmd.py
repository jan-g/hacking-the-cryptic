from .grid import Grid
from .display import display
from .constraints import constrain


grid1 = [".....H...",
         ".H.T....H",
         "......T.H",
         "..T......",
         "T.....H..",
         "T........",
         "......H..",
         ".T.......",
         ".........",
         ]


def main():
    g = Grid(grid1)
    constrain(g)
    while g.solve():
        display(g)
        _ = input()
