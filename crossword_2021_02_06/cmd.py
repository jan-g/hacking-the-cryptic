from .grid import Grid
from .display import display
from .constraints import constrain


grid1 = ["#.#.#.#.#.#.#.#",
         "...............",
         "#.#.#.#.#.#.#.#",
         "......#........",
         "#.#.#.#.#.#.#.#",
         "........#......",
         "#.#####.#.#.###",
         ".......#.......",
         "###.#.#.#####.#",
         "......#........",
         "#.#.#.#.#.#.#.#",
         "........#......",
         "#.#.#.#.#.#.#.#",
         "...............",
         "#.#.#.#.#.#.#.#",
         ]
words1 = ["ACETATE",
          "BUDGIE SMUGGLERS",
          "CUISSE",
          "DIDDUMS",
          "ENCIRCLE",
          # Uncomment one of the following lines for different behaviour:
          "FLAMENCO", # The actual answer is "FANDANGO"; we'll place everything except this
          # "FANDANGO", # Put this in and you'll get a complete solution
          # "F......O", # This can be fit; the missing letters are still marked as unknown.
          "GREENISH",
          "HUMERI",
          "IPSO JURE",
          "JUNGLE",
          "LINGUIST",
          "KERATOID",
          "MUSIQUE CONCRETE",
          "NEGATE",
          "OTHERS",
          "PEAFOWL",
          "QUEENITE",
          "RHESUS",
          "SYZYGY",
          "TRIMETER",
          "URINAL",
          "VERTEBRA",
          "WALLOWED",
          "XIZANG",
          "YESHIVA",
          "ZONKEY",
          ]



def main():
    g = Grid(grid1, words=words1)
    constrain(g)
    while g.solve():
        display(g)
        if input() == "q":
            break
