# This file contais the visual part of the maze
# implementa o terminal interativo
# Marcar entry (E), exit (X) e caminho (.) quando solicitado
# Implementar o menu interativo:
#  1. Re-gerar maze  2. Show/Hide path  3. Mudar cor  4. Sair
from mazegen.generator import Direction
import os


def clear_and_reset() -> None:
    """Clean the screen and reset the Terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def draw_maze(grid: list[list[int]], horizontal_scale: int = 2) -> None:
    """Turn the render maze in a good aspect
    using 2 * x_position to match the y position"""
    scale = max(1, horizontal_scale)
    for line in grid:
        print("".join(str(ch) * scale for ch in line))


def convert_ascii(maze, wall_char: str = "█",
                  path_char: str = " ") -> list[list[str]]:
    """Convert the object maze into one ASCII representation.
    Each maze cell is expanted in a matrix of chars,
    where walls are representates by `wall_char` and paths are `path_char`.
    The origin coord is marked with 'E' and the exity with 'X'"""
    rows = maze.height * 2 + 1
    cols = maze.width * 2 + 1
    canvas = [[wall_char for i in range(cols)] for j in range(rows)]

    for r in range(maze.height):
        for c in range(maze.width):
            cell = maze.grid[r][c]
            cr = 2 * r + 1
            cc = 2 * c + 1
            canvas[cr][cc] = path_char

            if not cell.walls[Direction.NORTH]:
                canvas[cr - 1][cc] = path_char
            if not cell.walls[Direction.SOUTH]:
                canvas[cr + 1][cc] = path_char
            if not cell.walls[Direction.WEST]:
                canvas[cr][cc - 1] = path_char
            if not cell.walls[Direction.EAST]:
                canvas[cr][cc + 1] = path_char
        ox, oy = maze.origin
        fx, fy = maze.final
        ocr, occ = 2 * oy + 1, 2 * ox + 1
        fcr, fcc = 2 * fy + 1, 2 * fx + 1

        if 0 <= ocr < rows and 0 <= occ < cols:
            canvas[ocr][occ] = "E"
        if 0 <= fcr < rows and 0 <= fcc < cols:
            canvas[fcr][fcc] = "X"
    return canvas
