import os
import re
from typing import Dict, Any, Tuple, List, Optional

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "lib dotenv isnt installed, please run: "
        "python -m pip install python-dotenv"
    )


def _validate_format(archive: str) -> None:
    """Read the file and check if it follows the KEY=VALUE format."""
    try:
        with open(archive, 'r') as f:
            for i, line in enumerate(f.readlines(), 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if not re.match(r'^[^=]+=[^=]+$', line):
                    raise SyntaxError(f"Syntax error: line {i} not in KEY=VALUE format: '{line}'")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{archive}' not found.")


def _check_required_keys() -> None:
    """Verify if all mandatory keys exist in the environment."""
    keys: List[str] = [
        'WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT',
    ]
    for key in keys:
        if (os.getenv(key) is None and os.getenv(key.lower()) is None) or os.getenv(key) == "":
            raise ValueError(f"Missing required key '{key}' in config file")


def load_config(archive: str) -> Dict[str, Any]:
    """
    Load, parse and validate the maze configuration file.
    Returns a dictionary with validated parameters.
    """
    _validate_format(archive)
    load_dotenv(dotenv_path=archive)
    _check_required_keys()

    try:
        width_str = os.getenv('WIDTH') or os.getenv('width')
        height_str = os.getenv('HEIGHT') or os.getenv('height')
        entry_str = os.getenv('ENTRY') or os.getenv('entry')
        exit_str = os.getenv('EXIT') or os.getenv('exit')

        width: int = int(width_str) if width_str else 0
        height: int = int(height_str) if height_str else 0

        origin: Tuple[int, ...] = tuple(
            map(int, entry_str.split(','))
        ) if entry_str else (0, 0)

        final: Tuple[int, ...] = tuple(
            map(int, exit_str.split(','))
        ) if exit_str else (0, 0)

        output_file: Optional[str] = os.getenv('OUTPUT_FILE') \
            or os.getenv('output_file')
        perfect_raw: Optional[str] = os.getenv('PERFECT') \
            or os.getenv('perfect')

        perfect: Any = perfect_raw

        if str(perfect_raw).upper() == "TRUE":
            perfect = True
        elif str(perfect_raw).upper() == "FALSE":
            perfect = False

        if output_file == '':
            raise ValueError("Output_file config must cant be null")

    except ValueError as e:
        raise ValueError(f"Configuration error: {e}")

    try:
        if origin == final or origin > final:
            raise ValueError("Origin must be smaller than final")

        if (origin[0] >= width or origin[1] >= height
                or final[0] >= width or final[1] >= height):
            raise ValueError("Origin and final must be within the maze")

        if any(c < 0 for c in origin) or any(c < 0 for c in final):
            raise ValueError("Coordinates must be positive integers")

        if height < 0 or width < 0:
            raise ValueError("Maze dimensions must be positive integers")

        if perfect is not True and perfect is not False:
            raise ValueError("Perfect instruction must be True or False")

        return {
            "width": width,
            "height": height,
            "origin": origin,
            "final": final,
            "perfect": perfect
        }
    except ValueError as e:
        print(e)
        exit(1)
