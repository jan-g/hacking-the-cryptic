from .grid import Grid
from .display import display


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
    display(g)
