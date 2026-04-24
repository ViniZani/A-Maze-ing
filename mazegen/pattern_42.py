from typing import Any, Set, Tuple
from mazegen.types import Direction


def _set_edge(
    maze: Any,
    row: int,
    col: int,
    direction: Direction,
    is_open: bool
) -> None:
    """Open or close a direction between a cell and its neighbor."""
    direct_row, direct_col = direction.delta
    neig_row, neig_col = row + direct_row, col + direct_col

    if not (0 <= neig_row < maze.height and 0 <= neig_col < maze.width):
        return

    maze.grid[row][col].walls[direction] = not is_open
    maze.grid[neig_row][neig_col].walls[direction.opposite] = not is_open


def forty_two_mark(maze: Any) -> None:
    """
    Draw the 42 mark into the maze if it's possible.
    If the maze is too small, raises an error message.
    """
    if maze.width <= 10 or maze.height <= 7:
        print(
            "[ERROR] This size can't receive the 42 mark, "
            "please gen a bigger maze"
        )
        return

    pattern = [
        [1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
    ]

    center_row: int = maze.height // 2
    center_col: int = maze.width // 2
    beg_row: int = center_row - 2
    beg_col: int = center_col - 3

    protected: Set[Tuple[int, int]] = set()

    for i in range(5):
        for j in range(7):
            row: int = beg_row + i
            col: int = beg_col + j
            if pattern[i][j] == 0:
                continue

            protected.add((row, col))
            cell = maze.grid[row][col]
            cell.visited = True
            cell.is_pattern_mark = True

    for row_p, col_p in protected:
        for direction in Direction:
            _set_edge(maze, row_p, col_p, direction, False)

    maze.protected_cells = protected
