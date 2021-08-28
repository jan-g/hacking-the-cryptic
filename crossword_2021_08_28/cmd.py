from crossword_2021_02_06.grid import Grid
from crossword_2021_02_06.display import display
from crossword_2021_02_06.constraints import constrain


grid1 = ["###.#.#.#.#.#.#.#.#.###",
         "##......#.....#......##",
         "#.#.#.#.#.#.#.#.#.#.#.#",
         "........#.......#......",
         "#.#.#.#.#.#.#.#.###.#.#",
         ".......#........#......",
         "#.###.#.#.###.###.###.#",
         ".....#........#........",
         "###.###.###.###.#.#.#.#",
         "....#.....#.....#......",
         "#.#.#.#.#.#.#.#.#.#.###",
         "........#.....#........",
         "###.#.#.#.#.#.#.#.#.#.#",
         "......#.....#.....#....",
         "#.#.#.#.###.###.###.##.",
         "........#........#.....",
         "#.###.###.###.#.#.###.#",
         "......#........#.......",
         "#.#.###.#.#.#.#.#.#.#.#",
         "......#.......#........",
         "#.#.#.#.#.#.#.#.#.#.#.#",
         "##......#.....#......##",
         "###.#.#.#.#.#.#.#.#.###",
         ]

"""
Clues are in alphabetical order of their solutions, which are to be entered in the grid jigsaw-wise.
A theme is indicated by a two-word solution, not further defined. Fourteen more clues produce solutions,
also not defined, that are related to this theme. The one-word solution to a ‘normal’ clue is to be
entered in the grid in two parts. Reading clockwise around the perimeter from the bottom right-hand
square are the four parts that make up the theme.
"""

words1 = [
	".. ......",	# Throw it away blocking the road to King’s Lynn from the very start (2,6)
	"......",	# Torn skin from silver catch (6)
	"........",	# New chamberlain dismisses wretched man (8)
	"........",	# A chum having half an hour with first of scientific dabblers (8)
	"......",	# Personification of wisdom further consumed by case of anorexia (6)
	".....",	# Regularly finding many in shoot in Northamptonshire village (5)
	".....",	# A Himalayan crossbreed, one cold and lifeless (5)
	"........",	# Almost crazy — helps pub staff (8)
	"........",	# Lair a nob designed, in an old impressive style (8)
	"... ...",	# Petrified wood with antelope circling game area (3,3)
	"........",	# They support retirees (8)
	".........",	# Excited builder includes names on hospital (10)
	"........",	# Food sent back and, for Heinz, last of barley wine (8)
	"......",	# He’ll take drivers round the course (6)
	".....",	# Girl in chains? (5)
	"...",	# Caesar’s god’s only half the next one! (3)
	"...-....",	# Centrally, prices indeed unfrozen (2-4)
	".....",	# Librarian’s covered in tiny drops, so they say (5)
	"......",	# Gloomy donkey from central Greece, long ago (6)
	"......",	# Decadent sweetheart at s-social function (6)
	"...",	# Foreign article of inordinate interest (3)
	"......",	# Man of note somewhere offshore, embraced by HM (6)
	".......",	# In English wood, church camp (7)
	"......",	# Bather’s discovery call for Australian rebellion of 1854 (6)
	".....",	# Half the team including another for a period away from home (5)
	"......",	# False, false friend idles falsely away (6)
	"......",	# Milton’s brother with name which precedes Barnet (6)
	".......",	# Replete, having eaten spaghetti outside (and one other pasta) (7)
	"........",	# Nintendo video console ready with 8 or 27 (8)
	"......",	# Joined up threateningly on short river that’s deserted (6)
	"......",	# Cove’s hot spring, say (6)
	"........",	# Heed girl, when troubled (8)
	".... ....",	# Escapes and is not made to pay (4,4)
	".......",	# Professional killer’s instrument — not half! (7)
	".......",	# A French trug damaged first (7)
	".....",	# Half the capital goes missing (5)
	".....",	# Auditorium with English orchestra (5)
	".......",	# Harassing love — which leaves (7)
	"....",	# Afraid, left, having nothing to do (4)
	"......",	# One assessor is more incensed (6)
	".........",	# He takes off from Indian city, say, after strike (9)
	".....",	# Climber in central Italian Alps (5)
	"......",	# During the ’50s, university education settled down (6)
	".....",	# Historian lost deposit in gambling paradise (5)
	"........",	# Chap with mum’s dog (8)
	"......",	# Married giant — disastrous union (6)
	"........",	# Grandma with new canine indoors in Cheshire town (8)
	"....",	# Where lines meet new lines (4)
	".. ....",	# Taking a trip as far as old city (2,4)
	"........",	# Wrong tree having bark removed (8)
	".......",	# Not starting regular exercise in the wet (7)
	".... ....",	# Such drinks are a sell-out (4,4)
	"....",	# André the violinist swaps sides in place (4)
	".... .....",	# Call round (4,5)
	".........",	# Inside leg injured (9)
	"........",	# German victory letter (8)
	".....",	# This jargon is, on reflection, somewhat foreign, also (5)
	"... .... ..",	# Rudely waken to do art in Japan (3,4,2)
	"...... ....",	# Those wandering around Irish county town for trainer (6,4)
	"......",	# Outburst, as I got stuck in traffic (6)
	"......",	# Goethe’s dream a shock (6)
	"........",	# Caravan, which may be a danger to bathers (8)
	"......",	# Four in a lav? Not all in this one! (6)
	"......",	# Old leader from country area (6)
	".........",	# Scotsman’s choice includes fish, it’s said (9)
	".........",	# Firmly established, though parts of rod are missing (9)
	".....",	# Pilot’s badge for rock band in off-stage area (5)
	".....",	# Female (not male) but feminist finally instead (5)
          ]



def main():
    g = Grid(grid1, words=words1)
    constrain(g)
    while g.solve():
        display(g)
        if input() == "q":
            break
