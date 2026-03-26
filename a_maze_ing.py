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
from mazegen.writer import write_data

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
    # ==============
    # teste apenas
    print(f"width: {maze.width}")
    print(f"heigth: {maze.height}")
    print(f"origin: {maze.origin}")
    print(f"final: {maze.final}")
    maze.draw_cell(maze.origin[0], maze.origin[1], 'E')
    maze.draw_cell(maze.final[0], maze.final[1], 'S')
    maze.render()
    # ===========
    # write_hex_path()
    write_data(maze.origin[0], maze.origin[1], maze.final[0], maze.final[1])
    # write_cord_path()
