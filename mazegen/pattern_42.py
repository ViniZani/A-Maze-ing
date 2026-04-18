# logica de inserção da logo 42 no meio do labirinto
# Definir as coordenadas das células que formam os dígitos "4" e "2"
# Fechar todas as paredes dessas células (hex F = 1111)
# Verificar se o tamanho do maze permite o padrão
# Printar mensagem de erro se o maze for pequeno demais
from mazegen.generator import Direction


def _set_edge(maze, row: int, col: int, direction, is_open: bool) -> None:
    """Open or close a direction between a cell and his neighboor"""
    direct_row, direct_col = direction.delta
    neig_row, neig_col = row + direct_row, col + direct_col
    if not (0 <= neig_row < maze.height and 0 <= neig_col < maze.width):
        return
    maze.grid[row][col].walls[direction] = not is_open
    maze.grid[neig_row][neig_col].walls[direction.opposite] = not is_open


def forty_two_mark(maze) -> None:
    """Draw the 42 mark in to the maze if its possible,
    else, raise the error"""
    if maze.width <= 10 or maze.height <= 7:
        print("[ERROR] This side can't received the 42 mark,\
please gen a bigger maze")
        return

    pattern = [
        [1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
    ]

    center_row = maze.height // 2
    center_col = maze.width // 2
    beg_row = center_row - 2
    beg_col = center_col - 3
    protected = set()
    for i in range(5):
        for j in range(7):
            row = beg_row + i
            col = beg_col + j
            if pattern[i][j] == 0:
                continue
            protected.add((row, col))
            cell = maze.grid[row][col]
            cell.visited = True
            cell.is_pattern_mark = True
    for row, col in protected:
        for direction in Direction:
            _set_edge(maze, row, col, direction, False)
    maze.protected_cells = protected
