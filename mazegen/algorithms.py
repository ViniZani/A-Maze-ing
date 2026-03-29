# algortimos de geração de labirinto
# Começa numa célula qualquer, marca como visitada
# Olha os vizinhos não visitados
# Escolhe um aleatoriamente, remove a parede entre os dois
# Move para esse vizinho e repete
# Se não há vizinhos disponíveis, volta para a célula anterior (backtrack)
# Para quando todas as células foram visitadas
import random


def dfs_algoritm(grid):
    is_visited(grid)


def is_visited(grid):
    row = len(grid) - 2
    col = len(grid[0]) - 2
    start = []
    start.append(random.randint(0, row))
    start.append(random.randint(0, col))
    print(f"posição inicial: {start[0], start[1]}")
