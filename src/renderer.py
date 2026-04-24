import os
from time import sleep
from typing import Any, List
from mazegen.types import Direction


def clear_and_reset() -> None:
    """Clean the screen and reset the Terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def draw_maze(grid: List[List[Any]], horizontal_scale: int = 2) -> None:
    """
    Render the maze with a better aspect ratio.
    Uses a horizontal scale to match the vertical height of characters.
    """
    scale = max(1, horizontal_scale)
    for line in grid:
        print("".join(str(ch) * scale for ch in line))


def convert_ascii(maze: Any, scheme: Any) -> List[List[str]]:
    """
    Convert the maze into an ASCII representation.
    Each maze cell is expanded into a matrix of chars,
    where walls and paths are defined by the scheme.
    """
    rows: int = maze.height * 2 + 1
    cols: int = maze.width * 2 + 1
    canvas: List[List[str]] = [
        [scheme.wall for _ in range(cols)] for _ in range(rows)
    ]

    for r in range(maze.height):
        for c in range(maze.width):
            cell = maze.grid[r][c]
            cr, cc = 2 * r + 1, 2 * c + 1

            canvas[cr][cc] = (
                scheme.pattern if cell.is_pattern_mark else scheme.path
            )

            if not cell.walls[Direction.NORTH]:
                canvas[cr - 1][cc] = scheme.path
            if not cell.walls[Direction.SOUTH]:
                canvas[cr + 1][cc] = scheme.path
            if not cell.walls[Direction.WEST]:
                canvas[cr][cc - 1] = scheme.path
            if not cell.walls[Direction.EAST]:
                canvas[cr][cc + 1] = scheme.path

    o_r, o_c = maze.origin
    f_r, f_c = maze.final
    ocr, occ = 2 * o_r + 1, 2 * o_c + 1
    fcr, fcc = 2 * f_r + 1, 2 * f_c + 1

    if 0 <= ocr < rows and 0 <= occ < cols:
        canvas[ocr][occ] = scheme.origin
    if 0 <= fcr < rows and 0 <= fcc < cols:
        canvas[fcr][fcc] = scheme.exit

    return canvas


def animated_gen_maze(
    canvas: List[List[str]],
    horizontal_scale: int = 2
) -> None:
    """Print the maze line by line with animation and scaling."""
    scale = max(1, horizontal_scale)
    for line in canvas:
        formatted_line = "".join(str(cell) * scale for cell in line)
        print(formatted_line, flush=True)
        print("\a", end="", flush=True)
        sleep(0.05)


def size_validation(config_data: dict[str, Any]) -> bool:
    """
    Validate if the terminal window size is enough for the maze.
    Returns True if there is an error (insufficient space).
    """
    error = False
    try:
        window = os.get_terminal_size()
        maze_row_needed = (config_data['width'] * 2) + 1
        maze_col_needed = (config_data['height'] * 2) + 1

        if maze_row_needed > window.columns or maze_col_needed > window.lines:
            error = True
            raise ValueError(
                f"Terminal too small ({window.columns}x{window.lines}). "
                f"Needed at least {maze_row_needed}x{maze_col_needed}."
            )
    except (ValueError, OSError) as e:
        print(f"[ERROR]: {e}")
    return error
