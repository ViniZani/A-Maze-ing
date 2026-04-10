# This file contais the visual part of the maze
# implementa o terminal interativo
# Marcar entry (E), exit (X) e caminho (.) quando solicitado
# Implementar o menu interativo:
#  1. Re-gerar maze  2. Show/Hide path  3. Mudar cor  4. Sair
from mazegen.generator import Direction


def draw_cell(grid: list[list[int]], x: int, y: int, char: str):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        grid[y][x] = char


def draw_maze(grid: list[list[int]]):
    for line in grid:
        print(" ".join(map(str, line)))


def convert_ascii(maze, wall_char="█", path_char=" "):
    """
    Desenha o labirinto usando um canvas de caracteres.
    Cada célula ocupa uma posição central em (2*r+1, 2*c+1).
    Paredes ocupam as posições entre centros.
    """
    rows = maze.height * 2 + 1
    cols = maze.width * 2 + 1
    canvas = [[wall_char for i in range(cols)] for j in range(rows)]

    for r in range(maze.height):
        for c in range(maze.width):
            cell = maze.grid[r][c]
            cr = 2 * r + 1
            cc = 2 * c + 1
            if cell.ftchar is not None:
                canvas[cr][cc] = cell.ftchar
            else:
                canvas[cr][cc] = path_char

            if not cell.walls[Direction.NORTH]:
                canvas[cr - 1][cc] = path_char
            if not cell.walls[Direction.SOUTH]:
                canvas[cr + 1][cc] = path_char
            if not cell.walls[Direction.WEST]:
                canvas[cr][cc - 1] = path_char
            if not cell.walls[Direction.EAST]:
                canvas[cr][cc + 1] = path_char
    print(f"Canvas size: {len(canvas)}x{len(canvas[0])}, Accessing: {2*maze.final[0]+1}")
    canvas[2 * maze.origin[0] + 1][2 * maze.origin[1] + 1] = "O"
    canvas[2 * maze.final[0] + 1][2 * maze.final[1] + 1] = "X"
    return canvas
    # for line in canvas:
    #    print("".join(line))
