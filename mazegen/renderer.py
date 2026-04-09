# This file contais the visual part of the maze
# implementa o terminal interativo
# Marcar entry (E), exit (X) e caminho (.) quando solicitado
# Implementar o menu interativo:
#  1. Re-gerar maze  2. Show/Hide path  3. Mudar cor  4. Sair
from mazegen.algorithms import NORTH, SOUTH, EAST, WEST


def draw_cell(grid: list[list[int]], x: int, y: int, char: str):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        grid[y][x] = char


def draw_maze(grid: list[list[int]]):
    for line in grid:
        print(" ".join(map(str, line)))


def convert_ascii(grid: list[list[int]], width: int, height: int,
                  origin: tuple, final: tuple, wall_char="█", path_char=" "):
    """
    Desenha o labirinto usando um canvas de caracteres.
    Cada célula ocupa uma posição central em (2*r+1, 2*c+1).
    Paredes ocupam as posições entre centros.
    """
    rows = height * 2 + 1
    cols = width * 2 + 1
    canvas = [[wall_char for i in range(cols)] for j in range(rows)]

    for r in range(height):
        for c in range(width):
            cell = grid[r][c]
            cr = 2 * r + 1
            cc = 2 * c + 1
            canvas[cr][cc] = path_char

            if not (cell & NORTH):
                canvas[cr - 1][cc] = path_char
            if not (cell & SOUTH):
                canvas[cr + 1][cc] = path_char
            if not (cell & WEST):
                canvas[cr][cc - 1] = path_char
            if not (cell & EAST):
                canvas[cr][cc + 1] = path_char

    canvas[origin[0]][origin[1]] = "E"
    canvas[final[0]][final[0]] = "X"

    for line in canvas:
        print("".join(line))
