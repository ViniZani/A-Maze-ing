import sys
from time import sleep
from typing import Any, Dict, Tuple

from src.config_parser import load_config
from mazegen.generator import MazeGenerator
from mazegen.types import Colors
from src.renderer import (
    convert_ascii, draw_maze, size_validation,
    clear_and_reset, animated_gen_maze
)
from src.solver import solve_bfs, render_path, animated_path
from src.writer import write_data, write_hex_path, write_cord_path


def gen_maze(maze: Any, scheme: Colors, config_data: Dict[str, Any]) -> None:
    """Generate the maze logic, render it and save to a file."""
    maze.generate()

    clear_and_reset()
    canvas = convert_ascii(maze, scheme)
    if size_validation(config_data) is True:
        return
    draw_maze(canvas)

    write_hex_path(maze)
    write_data(maze.origin[0], maze.origin[1], maze.final[0], maze.final[1])
    path = solve_bfs(maze)
    write_cord_path(path)


def menu() -> None:
    """Interactive CLI menu to manage maze generation and visualization."""
    argv = sys.argv
    argc = len(argv)
    try:
        if argc == 2:
            config_data = load_config(argv[1])
        else:
            raise TypeError("Usage: python a_maze_ing.py config.txt")
    except Exception as e:
        print(f"[ERRO]: {e}")
        sys.exit(1)

    origin_coord: Tuple[int, int] = (
        config_data['origin'][1], config_data['origin'][0]
    )
    final_coord: Tuple[int, int] = (
        config_data['final'][1], config_data['final'][0]
    )

    maze = MazeGenerator(
        config_data['width'],
        config_data['height'],
        origin_coord,
        final_coord,
        config_data['perfect']
    )

    default_scheme = Colors(
        "\033[37m█\033[0m", " ", "\033[92m█\033[0m",
        "\033[91m█\033[0m", "█", "\033[94m█\033[0m"
    )

    colors_scheme = Colors(
        "\033[94m█\033[0m", " ", "\033[92m█\033[0m",
        "\033[91m█\033[0m", "\033[37m█\033[0m", "\033[93m█\033[0m"
    )

    hard_mode = Colors(
        "\033[91m█\033[0m", "\033[93m█\033[0m", "\033[30m█\033[0m",
        "\033[97m█\033[0m", "\033[38;5;208m█\033[0m", "\033[38;5;129m█\033[0m"
    )

    current_scheme = default_scheme
    show_path = False
    gen_maze(maze, current_scheme, config_data)

    while True:
        try:
            print("\n=== A-Maze-ing ===")
            print("1. Regenerate maze")
            print("2. Show/Hide path from entry to exit")
            print("3. Rotate Maze colors")
            print("4. Animated path")
            print("5. Animated Maze Generator")
            print("6. Exit")

            order = input("Choice (1-6): ").strip()

            if order == "1":
                show_path = False
                maze = MazeGenerator(
                    config_data['width'], config_data['height'],
                    origin_coord, final_coord, config_data['perfect']
                )
                gen_maze(maze, current_scheme, config_data)

            elif order == "2":
                clear_and_reset()
                canvas = convert_ascii(maze, current_scheme)
                if not show_path:
                    path = solve_bfs(maze)
                    render_path(canvas, path, current_scheme)
                    draw_maze(canvas)
                    show_path = True
                else:
                    draw_maze(canvas)
                    show_path = False

            elif order == "3":
                if current_scheme == default_scheme:
                    current_scheme = colors_scheme
                elif current_scheme == colors_scheme:
                    current_scheme = hard_mode
                else:
                    current_scheme = default_scheme
                clear_and_reset()
                canvas = convert_ascii(maze, current_scheme)
                if show_path:
                    path = solve_bfs(maze)
                    render_path(canvas, path, current_scheme)
                draw_maze(canvas)

            elif order == "4":
                clear_and_reset()
                canvas = convert_ascii(maze, current_scheme)
                path = solve_bfs(maze)
                animated_path(canvas, path, current_scheme)

            elif order == "5":
                clear_and_reset()
                canvas = convert_ascii(maze, current_scheme)
                animated_gen_maze(canvas)

            elif order == "6":
                print("Cleaning the cache", end="")
                for _ in range(3):
                    sleep(0.2)
                    print(".", end="")
                    sys.stdout.flush()
                print("\nExiting the maze!...")
                break
            else:
                print("\n[ERRO]: Please, choose between 1 and 6")

        except (ValueError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            break


if __name__ == "__main__":
    menu()
