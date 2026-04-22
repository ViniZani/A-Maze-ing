# This file contais the visual part of the maze
# implementa o terminal interativo
# Marcar entry (E), exit (X) e caminho (.) quando solicitado
# Implementar o menu interativo:
#  1. Re-gerar maze  2. Show/Hide path  3. Mudar cor  4. Sair
from mazegen.types import Direction
import os
from time import sleep


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


def convert_ascii(maze, scheme) -> list[list[str]]:
    """Convert the maze into one ASCII representation.
    Each maze cell is expanted in a matrix of chars,
    where walls are representates by `wall_char` and paths are `path_char`.
    The origin coord is marked with 'scheme.origin'
    and the exity with 'scheme.exit'"""
    rows = maze.height * 2 + 1
    cols = maze.width * 2 + 1
    canvas = [[scheme.wall for i in range(cols)] for j in range(rows)]

    for r in range(maze.height):
        for c in range(maze.width):
            cell = maze.grid[r][c]
            cr = 2 * r + 1
            cc = 2 * c + 1
            if cell.is_pattern_mark is True:
                canvas[cr][cc] = scheme.pattern
            else:
                canvas[cr][cc] = scheme.path

            if not cell.walls[Direction.NORTH]:
                canvas[cr - 1][cc] = scheme.path
            if not cell.walls[Direction.SOUTH]:
                canvas[cr + 1][cc] = scheme.path
            if not cell.walls[Direction.WEST]:
                canvas[cr][cc - 1] = scheme.path
            if not cell.walls[Direction.EAST]:
                canvas[cr][cc + 1] = scheme.path
    orow, ocol = maze.origin
    frow, fcol = maze.final

    ocr = 2 * orow + 1
    occ = 2 * ocol + 1
    fcr = 2 * frow + 1
    fcc = 2 * fcol + 1

    if 0 <= ocr < rows and 0 <= occ < cols:
        canvas[ocr][occ] = scheme.origin
    if 0 <= fcr < rows and 0 <= fcc < cols:
        canvas[fcr][fcc] = scheme.exit
    return canvas


def animated_gen_maze(canvas, scheme, horizontal_scale: int = 2):
    """Imprime o labirinto linha por linha com animação e escala."""
    scale = max(1, horizontal_scale)
    for line in canvas:
        formatted_line = "".join(str(cell) * scale for cell in line)
        print(formatted_line)
        sleep(0.1)
