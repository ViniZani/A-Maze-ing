# main do programa (python a_amze_ing.py conig.txt)
# Ler o argumento sys.argv[1] (config.txt)
# Chamar config_parser para carregar a config do txt
# Passar instancias do MazeGenerator com os parametros
# Chamar writer para salvar o output no output.txt
# Chamar renderer para exibir o labirinto com a lib grafica
# Tratar as exceptions
import sys
from mazegen.config_parser import load_config
from mazegen.generator import MazeGenerator
from mazegen.renderer import convert_ascii
from mazegen.algorithms import dfs_algoritm
from mazegen.writer import write_data, write_hex_path


def gen_maze(maze):
    # ============== teste apenas
    # print(f"width: {maze.width}")
    # print(f"heigth: {maze.height}")
    # print(f"origin: {maze.origin}")
    # print(f"final: {maze.final}")

    # draw_maze(maze.grid)
    # print("\n======================================\n")
    dfs_algoritm(maze.grid, maze.width, maze.height)
    # draw_maze(maze.grid)
    convert_ascii(maze.grid, maze.width, maze.height, maze.origin, maze.final)

    # ===========
    write_hex_path(maze.grid, maze.height, maze.width)
    write_data(maze.origin[0], maze.origin[1], maze.final[0], maze.final[1])
    # write_cord_path()


if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    try:
        if argc == 2:
            config_data = load_config(argv[1])
        else:
            raise TypeError("Input only 'config.txt' as a parameter")
    except (Exception, TypeError) as e:
        print(e)
        exit(1)

    maze = MazeGenerator(config_data['width'], config_data['height'],
                         config_data['origin'], config_data['final'],
                         config_data['perfect'])

    gen_maze(maze)
    while True:
        try:
            print("\n===A-Maze-ING===")
            print("1. Regenerate maze")
            print("2. Show/Hide path from entry to exit")
            print("3. Rotate Maze colors")
            print("4. Exit")
            order = input("Choise (1-4): ")
            possible_order = ["1", "2", "3", "4"]
            if order not in possible_order:
                raise ValueError("\n[ERRO]: Please, choise between 1 and 4")
            if order == "1":
                maze = MazeGenerator(config_data['width'],
                                     config_data['height'],
                                     config_data['origin'],
                                     config_data['final'],
                                     config_data['perfect'])
                gen_maze(maze)
            elif order == "2":
                pass
            elif order == "3":
                pass
            elif order == "4":
                break
        except ValueError as e:
            print(e)
