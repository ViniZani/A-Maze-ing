from typing import List, Optional, Tuple
from mazegen.types import Cell
from mazegen.pattern_42 import forty_two_mark
from mazegen.algorithms import dfs_algorithm, validate_maze, broke_cells


class MazeGenerator:
    """Class responsible for managing the maze structure and generation."""

    def __init__(
        self,
        width: int,
        height: int,
        origin: Tuple[int, int],
        final: Tuple[int, int],
        perfect: bool = True,
        seed: Optional[int] = None
    ) -> None:
        """Initialize the maze generator with dimensions and constraints."""
        self.width: int = width
        self.height: int = height
        self.origin: Tuple[int, int] = origin
        self.final: Tuple[int, int] = final
        self.perfect: bool = perfect
        self.seed: Optional[int] = seed
        self.grid: List[List[Cell]] = [
            [Cell(r, c) for c in range(width)] for r in range(height)
        ]
        self.protected_cells: List[Tuple[int, int]] = []

    def generate(self) -> List[List[Cell]]:
        """
        Call the functions to generate the maze using the DFS algorithm.
        Validates the requirements and adds the 42 pattern if possible.
        Returns the generated grid of cells.
        """
        validate_maze(self.grid)
        forty_two_mark(self)
        dfs_algorithm(self, self.seed)

        if not self.perfect:
            broke_cells(self, self.width, self.height)
        return self.grid
