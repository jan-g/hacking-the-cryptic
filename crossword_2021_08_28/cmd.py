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
	"AB INITIO",	# X Throw it away blocking the road to King’s Lynn from the very start (2,6)
	"AGNAIL",	# X   Torn skin from silver catch (6)	AG- 
	"ALBERICH",	# X New chamberlain dismisses wretched man (8)	
	"AMATEURS",	# X A chum having half an hour with first of scientific dabblers (8) 
	"ATHENA",	# X Personification of wisdom further consumed by case of anorexia (6)
	"AYNHO",	# X Regularly finding many in shoot in Northamptonshire village (5)
	"AZOIC",	# X A Himalayan crossbreed, one cold and lifeless (5)
	"BARMAIDS",	# X Almost crazy — helps pub staff (8)  BARMY BARKING BAR-..? BARMAIDS
	"BARONIAL",	# X Lair a nob designed, in an old impressive style (8)
	"BOG OAK",	# X Petrified wood with antelope circling game area (3,3)
	"BOLSTERS",	# X They support retirees (8)	BEDPOSTS?
	"BRUNNHILDE",	# X Excited builder includes names on hospital (10)   
	"BURGUNDY",	# X Food sent back and, for Heinz, last of barley wine (8)
	"CADDIE",	# X He’ll take drivers round the course (6)
	"DAISY",	# X Girl in chains? (5)
	"DEI",		# X Caesar’s god’s only half the next one! (3)	CUR? C-D  CAD CED CID COD CUD
	"DE-ICED",	# X Centrally, prices indeed unfrozen (2-4)  (SPLIT DEI and CED)
	"DEWEY",	# X Librarian’s covered in tiny drops, so they say (5)
	"EEYORE",	# X Gloomy donkey from central Greece, long ago (6)
	"EFFETE",	# X Decadent sweetheart at s-social function (6)	
	"EIN",		# X Foreign article of inordinate interest (3) 
	"EISLER",	# X Man of note somewhere offshore, embraced by HM (6)  E....R  EISLER
	"EPICENE",	# X In English wood, church camp (7)  e.i.e.e 
	"EUREKA",	# X Bather’s discovery call for Australian rebellion of 1854 (6)
	"EXILE",	# X Half the team including another for a period away from home (5) FORAY EXILE?
	"FAFNER",	# X False, false friend idles falsely away (6)
	"F.I.RN",	#   Milton’s brother with name which precedes Barnet (6)   FASOLT?
	"FUSILLI",	# X Replete, having eaten spaghetti outside (and one other pasta) (7)	
	"GAMECUBE",	# X Nintendo video console ready with 8 or 27 (8)  
	"GANGED",	# X Joined up threateningly on short river that’s deserted (6)	GANGED
	"GEEZER",	# X Cove’s hot spring, say (6)	GEYSER GEEZER
	"GERHILDE",	# X Heed girl, when troubled (8)  
	"GETS FREE",	# X Escapes and is not made to pay (4,4)
	"GUNTHER",	# X Professional killer’s instrument — not half! (7)
	"GUTRUNE",	# X A French trug damaged first (7)  GUTRUNE
	"HAGEN",	# X Half the capital goes missing (5) GWENT   HAGEN?
	"HALLE",	# X Auditorium with English orchestra (5)	HALLE
	"HUNDING",	# X Harassing love — which leaves (7)
	"IDLE",		# X Afraid, left, having nothing to do (4)	IDLE 
	"IRATER",	# X One assessor is more incensed (6)	IRATER
	"LAMPOONER",	# X He takes off from Indian city, say, after strike (9) 
	"LIANA",	# X Climber in central Italian Alps (5) LIANA
	"LULLED",	# X During the ’50s, university education settled down (6)  L L
	"MACAU",	# X Historian lost deposit in gambling paradise (5) MACAU(LAY)
	"MALEMUTE",	# X Chap with mum’s dog (8) MALAMUTE? 
	"MATING",	# X Married giant — disastrous union (6)  M
	"NANTWICH",	# X Grandma with new canine indoors in Cheshire town (8) NANTWICH
	"NODE",		# X Where lines meet new lines (4) NORN?	N--E
	"ON TOUR",	# X Taking a trip as far as old city (2,4)  ON TOUR
	"ORTLINDE",	# X Wrong tree having bark removed (8)
	"RAINING",	# X Not starting regular exercise in the wet (7) RA.....  
	"REAL ALES",	# X Such drinks are a sell-out (4,4)
	"RIEU",		# X André the violinist swaps sides in place (4)  R..U 
	"RING CYCLE",	# X Call round (4,5)
	"SIEGLINDE",	# X Inside leg injured (9)
	"SIEGRUNE",	# X German victory letter (8)
	"SLANG",	# X This jargon is, on reflection, somewhat foreign, also (5) S-N--?
	"TAE KWON DO",	# X Rudely waken to do art in Japan (3,4,2) TAE KWON DO
	"TENNIS SHOE",	# X Those wandering around Irish county town for trainer (6,4) 
	"TIRADE",	# X Outburst, as I got stuck in traffic (6) TIRADE
	"TRAUMA",	# X Goethe’s dream a shock (6)  T..U.A
	"UNDERTOW",	# X Caravan, which may be a danger to bathers (8)
	"URINAL",	# X Four in a lav? Not all in this one! (6)	URINAL
	"WALESA",	# X Old leader from country area (6)
	"WALTRAUTE",	# X Scotsman’s choice includes fish, it’s said (9)
	"WELLGUNDE",	# X Firmly established, though parts of rod are missing (9) WELLGUNDE
	"WINGS",	# X Pilot’s badge for rock band in off-stage area (5)
	"WOTAN",	# X Female (not male) but feminist finally instead (5)
          ]



def main():
    g = Grid(grid1, words=words1)
    constrain(g)
    while g.solve():
        display(g)
        if input() == "q":
            break
