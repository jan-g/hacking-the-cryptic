from collections import defaultdict
from z3 import And, Or, Not, If, Optimize

from .grid import strip, char_to_int


def constrain(g):
    everything_is_a_letter(g)
    place_words(g)
    best_solution(g)


def everything_is_a_letter(g):
    for x, y in g.coords():
        if (c := g.letter(x, y)) is not None:
            g.add(0 <= c)
            g.add(c <= 26)


def bool_to_int(b):
    return If(b, 1, 0)


def place_words(g):
    # Accumulate the layout of the grid
    length_to_places = defaultdict(list)
    for x, y in g.coords():
        for dx, dy in ((1, 0), (0, 1)):
            if g.letter(x, y) is None:
                continue
            # Is there a previous cell that's also fillable? If so, skip this one.
            if g.letter(x - dx, y - dy) is not None:
                continue
            # Is there a following cell? If not this cell is uninteresting
            if g.letter(x + dx, y + dy) is None:
                continue
            line = []
            cx, cy = x, y
            while (c := g.letter(cx, cy)) is not None:
                line.append(c)
                cx += dx
                cy += dy
            length_to_places[len(line)].append(line)

    for w in g.words:
        place_word(g, w, length_to_places)


def best_solution(g):
    # We want to place as many words as possible
    placed = sum(bool_to_int(g.placed(w)) for w in g.words)
    g.solver.maximize(placed)

    # It'll be faster without this but you'll get gibberish letters in the unconstrained cells of the grid.
    all_chars = sum(char for x, y in g.coords() if (char := g.letter(x, y)) is not None)
    g.solver.minimize(all_chars)


def place_word(g, w, places):
    placed = g.placed(w)
    w = strip(w)
    options = []
    for place in places[len(w)]:
        # Assert that we can place this word here
        options.append(And(placed, *((position == char_to_int(char)) for (position, char) in zip(place, w) if char.isalpha())))

    # It's always possible that this word doesn't fit in the grid.
    g.add(Or(Not(placed), *options))
