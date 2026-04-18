# gera de fato o labirinto
# classe MazeGenertor obrigatoria
from enum import Enum


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


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 4
    WEST = 8

    @property
    def opposite(self) -> None:
        opposite_direct = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST
        }
        return opposite_direct[self]

    @property
    def delta(self) -> None:
        dif_direct = {
            Direction.NORTH: (-1, 0),
            Direction.SOUTH: (1, 0),
            Direction.EAST: (0, 1),
            Direction.WEST: (0, -1)
        }
        return dif_direct[self]


class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.visited = False
        self.is_pattern_mark = False
        self.walls = {
            Direction.NORTH: True,
            Direction.SOUTH: True,
            Direction.EAST: True,
            Direction.WEST: True
        }
        self.neighbors = {}

    def connected(self, other_cell: bool, direction: Direction) -> None:
        self.walls[direction] = False
        other_cell.walls[direction.opposite] = False
