# parte visual do labirinto
# implementa o terminal interativo
# Marcar entry (E), exit (X) e caminho (.) quando solicitado
# Implementar o menu interativo:
#  1. Re-gerar maze  2. Show/Hide path  3. Mudar cor  4. Sair
NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8


def draw_cell(grid: list[list], x: int, y: int, char: str):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        grid[y][x] = char


def add_border(grid, width, height) -> list[list]:
    border_grid = [[15] * (width + 2) for _ in range(height + 2)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            border_grid[i + 1][j + 1] = grid[i][j]
    grid = border_grid
    return grid


def draw_maze(grid):
    for line in grid:
        print(" ".join(map(str, line)))



"""def draw_maze(grid):
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        linha = ""
        for col in range(width):
            cell = grid[row][col]

            # checa cada parede da célula
            norte = cell & NORTH  # != 0 se fechada
            leste = cell & EAST
            sul   = cell & SOUTH
            oeste = cell & WEST

            # por enquanto só printa o hex de cada célula
            linha += f"{cell:X} "
        print(linha)"""
