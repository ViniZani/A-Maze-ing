# At this File you will find all the logic to generate mazes
# perfects (one path away) and inperfects (plus then one path)
# The DFS algorithm just generate a perfect maze
# To generate inperfect mazes, it must broke the walls randomly
from random import random, shuffle, randint, choice
from mazegen.types import Direction


def dfs_algorithm(maze, seed=None) -> None:
    """Startint at the origin, initialize the algorithm DFS"""
    if seed is not None:
        random.seed(seed)
    start_row = maze.origin[0]
    start_col = maze.origin[1]
    carve_cells(maze, start_row, start_col)


def carve_cells(maze, row, col) -> None:
    """Carve one of the directions of the maze's cells by the the DFS"""
    current_cell = maze.grid[row][col]
    current_cell.visited = True
    directions = list(Direction)
    shuffle(directions)
    for direction in directions:
        direct_row, direct_col = direction.delta
        new_row, new_col = row + direct_row, col + direct_col
        if 0 <= new_row < maze.height and 0 <= new_col < maze.width:
            neighbor = maze.grid[new_row][new_col]
            if not neighbor.visited:
                current_cell.connected(neighbor, direction)
                carve_cells(maze, new_row, new_col)


def broke_cells(maze, width: int, height: int) -> None:
    """Broke cells randomly to turn a perfect maze an inperfect"""
    break_count = round(width * height * 0.5)
    protected = getattr(maze, "protected_cells", set())
    for _ in range(break_count):
        row = randint(0, height - 2)
        col = randint(0, width - 2)
        if (row, col) in protected:
            continue
        current = maze.grid[row][col]
        if current.is_pattern_mark:
            continue
        direction = choice(list(Direction))
        direct_row, direct_col = direction.delta
        neighbor_row, neighbor_col = row + direct_row, col + direct_col
        if 0 <= neighbor_row < height and 0 <= neighbor_col < width:
            if (neighbor_row, neighbor_col) in protected:
                continue
            neighbor = maze.grid[neighbor_row][neighbor_col]
            if neighbor.is_pattern_mark:
                continue
            current.connected(neighbor, direction)


def validate_maze(grid) -> None:
    """Valids if the maze can't has large open areas.
    Corridors can't be wider than 2 cells. For example,
    you can have 2x3 or 3x2 open area, but never a 3x3 open area."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            block = [grid[r+i][c:c+3] for i in range(3)]
            open_cells = sum(cell == 0 for row in block for cell in row)
            if open_cells == 9:
                raise ValueError(
                    f"[ERRO]: área 3x3 aberta encontrada"
                    f"starting in ({r}, {c})")
