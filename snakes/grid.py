class Grid:
    def __init__(self, lines):
        self.grid = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self.grid[x, y] = char
