# logica de inserção da logo 42 no meio do labirinto
# Definir as coordenadas das células que formam os dígitos "4" e "2"
# Fechar todas as paredes dessas células (hex F = 1111)
# Verificar se o tamanho do maze permite o padrão
# Printar mensagem de erro se o maze for pequeno demais
from mazegen.generator import Direction


def forty_two_mark(maze):
    try:
        if maze.width <= 10 or maze.height <= 7:
            raise ValueError("[ERROR] This side can't recieved the 42 mark,"
                             "please gen a bigger maze")
        pattern = [[1, 0, 0, 0, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 0, 1, 1, 1],
                   [0, 0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 1, 1, 1]]
        center_x = maze.height//2
        center_y = maze.width//2
        beg_line = center_x - 2
        beg_col = center_y - 3
        for i in range(5):
            for j in range(7):
                cell = maze.grid[beg_line + i][beg_col + j]
                if pattern[i][j] == 0:
                    for directions in Direction:
                        cell.walls[directions] = False
                        cell.ftchar = "#"
                if pattern[i][j] == 1:
                    for directions in Direction:
                        cell.walls[directions] = True
    except ValueError as e:
        print(e)
