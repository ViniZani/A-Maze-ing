import os
from mazegen.types import Direction, Cell


def conv_cell_hex(cell: Cell):
    val = 0
    if cell.walls[Direction.NORTH] is True:
        val += Direction.NORTH.value
    if cell.walls[Direction.SOUTH] is True:
        val += Direction.SOUTH.value
    if cell.walls[Direction.EAST] is True:
        val += Direction.EAST.value
    if cell.walls[Direction.WEST] is True:
        val += Direction.WEST.value
    return val


def write_hex_path(maze):
    """Write the maze in hexadecimal chars in the file"""
    with open(os.getenv('OUTPUT_FILE'), 'w', encoding='utf-8') as archive:
        for i in range(maze.height):
            for j in range(maze.width):
                archive.write(f"{conv_cell_hex(maze.grid[i][j]):X}")
            archive.write("\n")


def write_data(origin_x, origin_y, final_x, final_y):
    """Write the origin and final cartesian's coordinates in the file"""
    content = f"\n{origin_x},{origin_y}\n{final_x},{final_y}\n"
    with open(os.getenv('OUTPUT_FILE'), 'a', encoding='utf-8') as archive:
        archive.write(content)


def cardinal_path(path):
    coord_path = []
    for i in range(len(path) - 1):
        curr_cell = path[i]
        next_cell = path[i+1]
        if next_cell[0] < curr_cell[0]:
            coord_path.append("N")
        elif next_cell[0] > curr_cell[0]:
            coord_path.append("S")
        elif next_cell[1] > curr_cell[1]:
            coord_path.append("E")
        elif next_cell[1] < curr_cell[1]:
            coord_path.append("W")
    return coord_path


def write_cord_path(path):
    """Write the best path direct's coordinates in the file"""
    coord_path = cardinal_path(path)
    # for check if the path is wirte:
    # print(f"The Cardinal Path is: {coord_path}")
    with open(os.getenv('OUTPUT_FILE'), 'a', encoding='utf-8') as archive:
        for i in range(len(coord_path)):
            archive.write(coord_path[i])
        archive.write("\n")
