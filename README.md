# From the "Snake on a Plane!" episode of "Cracking the Cryptic"

https://www.youtube.com/watch?v=47zaMkD7FCI

The puzzles are taken from here: https://logic-masters.de/Raetselportal/Raetsel/zeigen.php?id=0004ZB
and are credited to [Eggr](https://logic-masters.de/Raetselportal/Benutzer/allgemein.php?name=Eggr)

This uses the excellent Z3 SMT solver.


## Grauniad prize crossword, 2021-02-06

Here: https://www.theguardian.com/crosswords/2021/feb/06/prize-crossword-no-28362

This involves solving the clues, then fitting the words into a grid. What's interesting when
using Z3 as a support tool for this is dealing with situations where some of the proposed
answers are wrong (and don't fit). Maximise the words placed.
