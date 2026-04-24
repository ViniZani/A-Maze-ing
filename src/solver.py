from typing import List, Tuple, Optional, Dict, Any
from time import sleep
from mazegen.types import Direction
from src.renderer import draw_maze, clear_and_reset


def solve_bfs(maze: Any) -> List[Tuple[int, int]]:
    """
    Solve the maze using the Breadth-First Search (BFS) algorithm.
    Returns the shortest path as a list of (row, col) coordinates.
    """
    for row in maze.grid:
        for cell in row:
            cell.explored = False

    s_row, s_col = maze.origin
    e_row, e_col = maze.final
    queue: List[Tuple[int, int]] = [(s_row, s_col)]
    maze.grid[s_row][s_col].explored = True
    path_map: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {
        (s_row, s_col): None
    }
    found: bool = False

    while queue:
        curr_r, curr_c = queue.pop(0)
        if (curr_r, curr_c) == (e_row, e_col):
            found = True
            break

        cell = maze.grid[curr_r][curr_c]
        for direction in Direction:
            if cell.walls[direction] is False:
                dr, dc = direction.delta
                nr, nc = curr_r + dr, curr_c + dc

                if 0 <= nr < maze.height and 0 <= nc < maze.width:
                    neighbor = maze.grid[nr][nc]
                    if not neighbor.explored:
                        neighbor.explored = True
                        path_map[(nr, nc)] = (curr_r, curr_c)
                        queue.append((nr, nc))

    path: List[Tuple[int, int]] = []
    if found:
        curr: Optional[Tuple[int, int]] = (e_row, e_col)
        while curr is not None:
            path.append(curr)
            curr = path_map[curr]
        path.reverse()
    else:
        print("Path NOT found!")
    return path


def render_path(
    canvas: List[List[str]],
    path: List[Tuple[int, int]],
    scheme: Any
) -> None:
    """Mark the solved path on the ASCII canvas."""
    if not path:
        return

    for i in range(len(path)):
        r, c = path[i]
        cr, cc = 2 * r + 1, 2 * c + 1

        if canvas[cr][cc] not in [scheme.origin, scheme.exit]:
            canvas[cr][cc] = scheme.solver_path

        if i > 0:
            pr, pc = path[i - 1]
            mr = (2 * r + 1 + 2 * pr + 1) // 2
            mc = (2 * c + 1 + 2 * pc + 1) // 2
            if canvas[mr][mc] not in [scheme.origin, scheme.exit]:
                canvas[mr][mc] = scheme.solver_path


def animated_path(
    canvas: List[List[str]],
    path: List[Tuple[int, int]],
    scheme: Any
) -> None:
    """Display the solution path with a frame-by-frame animation."""
    for i in range(len(path)):
        r, c = path[i]
        cr, cc = 2 * r + 1, 2 * c + 1

        if canvas[cr][cc] not in [scheme.origin, scheme.exit]:
            canvas[cr][cc] = scheme.solver_path

        if i > 0:
            pr, pc = path[i - 1]
            mr = (2 * r + 1 + 2 * pr + 1) // 2
            mc = (2 * c + 1 + 2 * pc + 1) // 2
            if canvas[mr][mc] not in [scheme.origin, scheme.exit]:
                canvas[mr][mc] = scheme.solver_path

        draw_maze(canvas)
        sleep(0.1)
        if i < len(path) - 1:
            clear_and_reset()
