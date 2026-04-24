from __future__ import annotations
from enum import Enum
from typing import Dict, Tuple


class Direction(Enum):
    """Enum representing the four cardinal directions and their properties."""

    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    @property
    def opposite(self) -> Direction:
        """Return the opposite direction."""
        opposite_map: Dict[Direction, Direction] = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST
        }
        return opposite_map[self]

    @property
    def delta(self) -> Tuple[int, int]:
        """Return the (row_offset, col_offset) for the direction."""
        delta_map: Dict[Direction, Tuple[int, int]] = {
            Direction.NORTH: (-1, 0),
            Direction.EAST: (0, 1),
            Direction.SOUTH: (1, 0),
            Direction.WEST: (0, -1)
        }
        return delta_map[self]


class Cell:
    """Represent a single cell in the maze grid."""

    def __init__(self, row: int, col: int) -> None:
        """Initialize a cell with its coordinates and closed walls."""
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
        self.neighbors: Dict[Direction, Cell] = {}

    def connected(self, other_cell: Cell, direction: Direction) -> None:
        """Connect this cell to another by removing the shared wall."""
        self.walls[direction] = False
        other_cell.walls[direction.opposite] = False


class Colors:
    """Store the visual representation (ASCII/Colors) for the renderer."""

    def __init__(
        self,
        wall: str,
        path: str,
        origin: str,
        exit_point: str,
        pattern: str,
        solver_path: str
    ) -> None:
        """Initialize the color/character palette for rendering."""
        self.wall: str = wall
        self.path: str = path
        self.origin: str = origin
        self.exit: str = exit_point
        self.pattern: str = pattern
        self.solver_path: str = solver_path
