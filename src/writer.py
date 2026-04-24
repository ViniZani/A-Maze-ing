import os
from typing import Any, List, Tuple, Optional
from mazegen.types import Direction, Cell


def conv_cell_hex(cell: Cell) -> int:
    """Convert the cell's wall configuration to an integer bitmask (0-15)."""
    val = 0
    if cell.walls[Direction.NORTH]:
        val += Direction.NORTH.value
    if cell.walls[Direction.SOUTH]:
        val += Direction.SOUTH.value
    if cell.walls[Direction.EAST]:
        val += Direction.EAST.value
    if cell.walls[Direction.WEST]:
        val += Direction.WEST.value
    return val


def write_hex_path(maze: Any) -> None:
    """Write the maze grid as hexadecimal characters to the output file."""
    output_file: Optional[str] = os.getenv('OUTPUT_FILE')
    if not output_file:
        return

    with open(output_file, 'w', encoding='utf-8') as archive:
        for i in range(maze.height):
            for j in range(maze.width):
                archive.write(f"{conv_cell_hex(maze.grid[i][j]):X}")
            archive.write("\n")


def write_data(
    origin_row: int,
    origin_col: int,
    final_row: int,
    final_col: int
) -> None:
    """Write the origin and final coordinates in X,Y format to the file."""
    output_file: Optional[str] = os.getenv('OUTPUT_FILE')
    if not output_file:
        return
    content = f"\n{origin_col},{origin_row}\n{final_col},{final_row}\n"
    with open(output_file, 'a', encoding='utf-8') as archive:
        archive.write(content)


def cardinal_path(path: List[Tuple[int, int]]) -> List[str]:
    """Convert a list of coordinates into a list of cardinal directions."""
    coord_path: List[str] = []
    for i in range(len(path) - 1):
        curr_cell = path[i]
        next_cell = path[i + 1]

        if next_cell[0] < curr_cell[0]:
            coord_path.append("N")
        elif next_cell[0] > curr_cell[0]:
            coord_path.append("S")
        elif next_cell[1] > curr_cell[1]:
            coord_path.append("E")
        elif next_cell[1] < curr_cell[1]:
            coord_path.append("W")
    return coord_path


def write_cord_path(path: List[Tuple[int, int]]) -> None:
    """Write the cardinal direction path (N, S, E, W) to the output file."""
    output_file: Optional[str] = os.getenv('OUTPUT_FILE')
    if not output_file:
        return

    coord_path = cardinal_path(path)
    with open(output_file, 'a', encoding='utf-8') as archive:
        for direction in coord_path:
            archive.write(direction)
        archive.write("\n")
