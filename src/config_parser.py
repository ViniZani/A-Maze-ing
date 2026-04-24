# Lê e valida o arquivo de configuração KEY=VALUE.
# Ignorar linhas com #
# Parsear as KEYS do txt WIDTH, HEIGHT, ENTRY, EXIT, OUTPUT_FILE, PERFECT
# Validar os valores são coerentes (entry != exit, dentro das bordar)
# Retornar um dict com os parâmetros validados
# Dar Raise em exceções do contexto (so pode int postivio)
import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("lib dotenv isnt installed, please run: \
    python -m pip install python-dotenv")


def _validate_format(archive: str) -> None:
    try:
        with open(archive, 'r') as f:
            for i, line in enumerate(f.readlines(), 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' not in line:
                    print(f"Error: line {i} not in KEY=VALUE format: '{line}'")
                    exit(1)
    except FileNotFoundError:
        print(f"Error: file '{archive}' not found")
        exit(1)


def _check_required_keys() -> None:
    for key in ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT']:
        if os.getenv(key) is None:
            print(f"Error: missing required key '{key}' in config file")
            exit(1)


def load_config(archive) -> None:
    _validate_format(archive)
    load_dotenv(dotenv_path=archive)
    _check_required_keys()
    try:
        width = int(os.getenv('WIDTH'))
        height = int(os.getenv('HEIGHT'))
        origin = tuple(map(int, os.getenv('ENTRY').split(',')))
        final = tuple(map(int, os.getenv('EXIT').split(',')))
        output_file = os.getenv('OUTPUT_FILE')
        perfect = os.getenv('PERFECT')
        possibilty_perfect = [True, False, "True", "False", "true", "false"]
        if perfect == "True" or perfect == "true":
            perfect = True
        elif perfect == "False" or perfect == "false":
            perfect = False
        if output_file == '':
            raise ValueError("Output_file config must cant be null")
    except (Exception, ValueError) as e:
        print(e)
        exit(1)
    try:
        if origin == final or origin > final:
            raise ValueError("Origin must be smaller than final")
        elif (origin[0] >= width or origin[1] >= height
              or final[0] >= width or final[1] >= height):
            raise ValueError("Origin and final must be within "
                             "the interval of the maze")
        elif origin[0] < 0 or origin[1] < 0 or final[0] < 0 or final[1] < 0:
            raise ValueError("Coordinates must be input as positive integers")
        elif height < 0 or width < 0:
            raise ValueError("Maze dimension's must be input as positive\
                             integers")
        if perfect not in possibilty_perfect:
            raise ValueError("Perfect instruction must be True or False")
        else:
            return {"width": width,
                    "height": height,
                    "origin": origin,
                    "final": final,
                    "perfect": perfect}
    except (Exception, ValueError) as e:
        print(e)
        exit(1)
