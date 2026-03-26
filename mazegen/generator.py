# gera de fato o labirinto


class MazeGenerator:
    def __init__(self, width, height, origin, final, perfect=True, seed=None):
        self.width = width
        self.height = height
        self.origin = origin
        self.final = final
        self.perfect = perfect
        self.seed = seed
        self.grid = [["#" for _ in range(width)] for _ in range(height)]

    def draw_cell(self, x, y, char):
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            self.grid[y][x] = char

    def render(self):
        for line in self.grid:
            print(" ".join(line))
