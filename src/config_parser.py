import os
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
                if '=' not in line:
                    print(f"Error: line {i} not in KEY=VALUE format: '{line}'")
                    exit(1)
    except FileNotFoundError:
        print(f"Error: file '{archive}' not found")
        exit(1)


def _check_required_keys() -> None:
    """Verify if all mandatory keys exist in the environment."""
    keys: List[str] = [
        'WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT'
    ]
    for key in keys:
        if os.getenv(key) is None:
            print(f"Error: missing required key '{key}' in config file")
            exit(1)


def load_config(archive: str) -> Dict[str, Any]:
    """
    Load, parse and validate the maze configuration file.

    Returns a dictionary with validated parameters.
    """
    _validate_format(archive)
    load_dotenv(dotenv_path=archive)
    _check_required_keys()

    try:
        # Casts e checks para satisfazer o Mypy (os.getenv pode ser None)
        width_str = os.getenv('WIDTH')
        height_str = os.getenv('HEIGHT')
        entry_str = os.getenv('ENTRY')
        exit_str = os.getenv('EXIT')

        width: int = int(width_str) if width_str else 0
        height: int = int(height_str) if height_str else 0

        # Conversão de coordenadas (Tuple[int, int])
        origin: Tuple[int, ...] = tuple(
            map(int, entry_str.split(','))
        ) if entry_str else (0, 0)

        final: Tuple[int, ...] = tuple(
            map(int, exit_str.split(','))
        ) if exit_str else (0, 0)

        output_file: Optional[str] = os.getenv('OUTPUT_FILE')
        perfect_raw: Optional[str] = os.getenv('PERFECT')

        # Lógica de conversão do booleano PERFECT
        perfect: Any = perfect_raw
        possibility_perfect: List[Any] = [
            True, False, "True", "False", "true", "false"
        ]

        if perfect_raw in ["True", "true"]:
            perfect = True
        elif perfect_raw in ["False", "false"]:
            perfect = False

        if output_file == '':
            raise ValueError("Output_file config must cant be null")

    except ValueError as e:
        print(f"Configuration error: {e}")
        exit(1)

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

        if perfect not in possibility_perfect:
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
