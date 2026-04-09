# At this File you will find all the logic to generate mazes
# perfects (one path away) and inperfects (plus then one path)
# The DFS algorithm just generate a perfect maze
# To generate inperfect mazes, it must broke the walls randomly
import random

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

DIRECTION = [NORTH, SOUTH, EAST, WEST]
OPPOSITE = {NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}

DELTA = {NORTH: (-1, 0), SOUTH: (1, 0), EAST:  (0, 1), WEST:  (0, -1)}


def dfs_algoritm(grid, width, height, seed=None, perfect=True):
    if seed is not None:
        random.seed(seed)
    visited = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append(False)
        visited.append(line)
    start_row = random.randint(0, height-1)
    start_col = random.randint(0, width-1)
    carve_cells(grid, visited, width, height, start_row, start_col)
    if perfect is False:
        broke_cells(grid, width, height)


def carve_cells(grid, visited, width, height, row, col):
    visited[row][col] = True
    directions = DIRECTION[:]
    random.shuffle(directions)
    for direct in directions:
        new_row = row + DELTA[direct][0]
        new_col = col + DELTA[direct][1]
        if 0 <= new_row < height and 0 <= new_col < width:
            if visited[new_row][new_col] is False:
                grid[row][col] &= ~direct
                grid[new_row][new_col] &= ~OPPOSITE[direct]
                carve_cells(grid, visited, width, height, new_row, new_col)


def broke_cells(grid, width, height):
    """quebra lados aleatorio de celular aleatorias"""
    pass


def valdatin_maze(grid):
    """valida se The maze can’t have large open areas.
    Corridors can’t be wider than 2 cells. For example,
    you can have 2x3 or 3x2 open area, but never a 3x3 open area."""
    pass
