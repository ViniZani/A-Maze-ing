import sys
from mazegen.config_parser import load_config
from mazegen.generator import MazeGenerator
from mazegen.algorithms import dfs_algorithm, broke_cells, validate_maze
from mazegen.pattern_42 import forty_two_mark
from mazegen.renderer import convert_ascii, draw_maze, clear_and_reset
from mazegen.writer import write_data, write_hex_path


def gen_maze(maze):
    # ============== teste apenas
    # print(f"width: {maze.width}")
    # print(f"heigth: {maze.height}")
    # print(f"origin: {maze.origin}")
    # print(f"final: {maze.final}")
    if (maze.perfect is False):
        print("Its a false maze")
    forty_two_mark(maze)
    validate_maze(maze.grid)
    dfs_algorithm(maze)
    if maze.perfect is False:
        broke_cells(maze, maze.width, maze.height)
    clear_and_reset()
    # so p checkar a logica do false maze
    # if maze.perfect is False:
    #   print("Its a false maze")
    canvas = convert_ascii(maze)
    draw_maze(canvas)
    write_hex_path(maze)
    write_data(maze.origin[0], maze.origin[1], maze.final[0], maze.final[1])
    # write_cord_path()


def valid_input():
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
                # chama a funcao que exibe o melhor caminho
                pass
            elif order == "3":
                # chama funcao que muda as cores do maze
                pass
            elif order == "4":
                break
        except (ValueError, KeyboardInterrupt) as e:
            print(e)
