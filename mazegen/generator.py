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
        self.grid = [[15] * width for i in range(height)]
