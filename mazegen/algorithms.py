# At this File you will find all the logic to generate mazes
# perfects (one path away) and inperfects (plus then one path)
# The DFS algorithm just generate a perfect maze
# To generate inperfect mazes, it must broke the walls randomly
from random import random, shuffle, randint
from mazegen.generator import Direction


def dfs_algorithm(maze, seed=None):
    if seed is not None:
        random.seed(seed)
    start_row = maze.origin[0]
    start_col = maze.origin[1]
    carve_cells(maze, start_row, start_col)


def carve_cells(maze, row, col):
    current_cell = maze.grid[row][col]
    current_cell.visited = True

    directions = list(Direction)
    shuffle(directions)

    for direction in directions:
        dr, dc = direction.delta
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < maze.height and 0 <= new_col < maze.width:
            neighbor = maze.grid[new_row][new_col]
            if not neighbor.visited:
                current_cell.connected(neighbor, direction)
                carve_cells(maze, new_row, new_col)


def broke_cells(maze, width, height):
    print("Is a Inperfect maze, lets broke it!")
    break_cells = round(width * height * 0.2)
    for _ in range(break_cells):
        rand_x = randint(0, width - 1)
        rand_y = randint(0, height - 1)
        carve_cells(maze, rand_x, rand_y) # não fazer isso, gera recursividade infinita!!!! # noqa


def validate_maze(grid):
    """valida se The maze can't have large open areas.
    Corridors can't be wider than 2 cells. For example,
    you can have 2x3 or 3x2 open area, but never a 3x3 open area."""
    pass
