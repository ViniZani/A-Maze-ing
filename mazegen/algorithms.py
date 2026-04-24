import random
from typing import Any, Optional, List, Set
from mazegen.types import Direction


def dfs_algorithm(maze: Any, seed: Optional[int] = None) -> None:
    """Starting at the origin, initialize the algorithm DFS."""
    if seed is not None:
        random.seed(seed)

    start_row: int = maze.origin[0]
    start_col: int = maze.origin[1]
    carve_cells(maze, start_row, start_col)


def carve_cells(maze: Any, row: int, col: int) -> None:
    """Carve the directions of the maze's cells using DFS."""
    current_cell = maze.grid[row][col]
    current_cell.visited = True
    directions = list(Direction)
    random.shuffle(directions)

    for direction in directions:
        direct_row, direct_col = direction.delta
        new_row, new_col = row + direct_row, col + direct_col

        if 0 <= new_row < maze.height and 0 <= new_col < maze.width:
            neighbor = maze.grid[new_row][new_col]
            if not neighbor.visited:
                current_cell.connected(neighbor, direction)
                carve_cells(maze, new_row, new_col)


def broke_cells(maze: Any, width: int, height: int) -> None:
    """Broke cells randomly to turn a perfect maze into an imperfect one."""
    break_count: int = round(width * height * 0.5)
    protected: Set[tuple[int, int]] = getattr(maze, "protected_cells", set())

    for _ in range(break_count):
        row: int = random.randint(0, height - 2)
        col: int = random.randint(0, width - 2)

        if (row, col) in protected:
            continue

        current = maze.grid[row][col]
        if current.is_pattern_mark:
            continue

        direction = random.choice(list(Direction))
        d_row, d_col = direction.delta
        neighbor_row, neighbor_col = row + d_row, col + d_col

        if 0 <= neighbor_row < height and 0 <= neighbor_col < width:
            if (neighbor_row, neighbor_col) in protected:
                continue

            neighbor = maze.grid[neighbor_row][neighbor_col]
            if neighbor.is_pattern_mark:
                continue

            current.connected(neighbor, direction)


def validate_maze(grid: List[List[Any]]) -> None:
    """
    Validate if the maze has large open areas.
    Corridors can't be wider than 2 cells. For example,
    you can have 2x3 or 3x2 open area, but never a 3x3 open area.
    """
    rows: int = len(grid)
    cols: int = len(grid[0]) if rows > 0 else 0

    for r in range(rows - 2):
        for c in range(cols - 2):
            block = [grid[r + i][c:c + 3] for i in range(3)]
            open_cells = sum(cell == 0 for row in block for cell in row)

            if open_cells == 9:
                raise ValueError(
                    f"[ERRO]: área 3x3 aberta encontrada "
                    f"starting in ({r}, {c})"
                )
