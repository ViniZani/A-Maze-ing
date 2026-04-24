from enum import Enum
from typing import Dict, Tuple


class Direction(Enum):
    NORTH = 1
    EAST  = 2
    SOUTH = 4
    WEST  = 8

    @property
    def opposite(self) -> 'Direction':
        opposite_direct: Dict[Direction, Direction] = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST
        }
        return opposite_direct[self]

    @property
    def delta(self) -> Tuple[int, int]:
        dif_direct = {
        Direction.NORTH: (-1, 0),
        Direction.EAST:  ( 0, 1),
        Direction.SOUTH: ( 1, 0),
        Direction.WEST:  ( 0,-1)
    }
        return dif_direct[self]


class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col
        self.visited: bool = False
        self.explored: bool = False
        self.is_pattern_mark: bool = False
        self.walls: Dict[Direction, bool] = {
            Direction.NORTH: True,
            Direction.SOUTH: True,
            Direction.EAST: True,
            Direction.WEST: True
        }
        self.neighbors: Dict[Direction, 'Cell'] = {}

    def connected(self, other_cell: 'Cell', direction: Direction) -> None:
        self.walls[direction] = False
        other_cell.walls[direction.opposite] = False


class Colors:
    def __init__(self, wall: str, path: str, origin: str,
                exit: str, pattern: str, solver_path: str) -> None:
        self.wall: str = wall
        self.path: str = path
        self.origin: str = origin
        self.exit: str = exit
        self.pattern: str = pattern
        self.solver_path: str = solver_path
