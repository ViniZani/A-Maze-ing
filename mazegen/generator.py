from mazegen.types import Cell
from mazegen.pattern_42 import forty_two_mark
from mazegen.algorithms import dfs_algorithm, validate_maze, broke_cells
# from src.solver import solve_bfs


class MazeGenerator:
    def __init__(self, width: int, height: int, origin: tuple,
                 final: tuple, perfect=True, seed=None):
        self.width = width
        self.height = height
        self.origin = origin
        self.final = final
        self.perfect = perfect
        self.seed = seed
        self.grid = [[Cell(r, c) for c in range(width)] for r in range(height)]

    def generate(self):
        """Calls the functions that will generate the maze using the
        DFS algorithm, validate if the maze is ok by the requirements
        and add the 42 pattern if it is possible"""
        validate_maze(self.grid)
        forty_two_mark(self)
        dfs_algorithm(self)

        if not self.perfect:
            broke_cells(self, self.width, self.height)

        # self.solution = solve_bfs(self)
        return self.grid
