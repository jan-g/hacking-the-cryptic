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


grid2 = [".........",
         "....H....",
         ".H..HH.T.",
         ".........",
         ".H.....H.",
         ".........",
         ".H.HH..T.",
         "....T....",
         ".........",
         ]


def main():
    g = Grid(grid2)
    constrain(g)
    while g.solve():
        display(g)
        if input() == "q":
            break
