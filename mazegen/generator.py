# gera de fato o labirinto
# classe MazeGenertor obrigatoria


class MazeGenerator:
    def __init__(self, width: int, height: int, origin: tuple, 
                 final: tuple, perfect=True, seed=None):
        self.width = width
        self.height = height
        self.origin = origin
        self.final = final
        self.perfect = perfect
        self.seed = seed
        self.grid = [["." for _ in range(width)] for _ in range(height)]

    def draw_cell(self, x: int, y: int, char: str):
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            self.grid[y][x] = char

    def add_border(self) -> list[list]:
        border_grid = [["#" for _ in range(self.width + 2)]
                       for _ in range(self.height + 2)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                border_grid[i + 1][j + 1] = self.grid[i][j]
        self.grid = border_grid

    def draw_maze(self) -> None:
        for line in self.grid:
            print(" ".join(line))
