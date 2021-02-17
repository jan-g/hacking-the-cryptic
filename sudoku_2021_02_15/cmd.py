from .grid import Grid
from .display import display
from .constraints import constrain


grid1 = ["... ... ...",
         "... ... ...",
         "... ... ...",

         "... ... ...",
         "... ... ...",
         "... ... ...",

         "... ... ...",
         "... ... ...",
         "... ... ...",
         ]


def main():
    g = Grid(grid1,
             columns=[22, 15, 13, 22, 17, 38, 42, 7, 20], rows=[13, 12, 20, 15, 27, 30, 41, 5, 33],
             head=(2, 5), tail=(8, 4))
    constrain(g)
    while g.solve():
        display(g)
        if input() == "q":
            break
