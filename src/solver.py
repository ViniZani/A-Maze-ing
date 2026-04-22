# Algortimo pra resolver o labritindo pelo melhor caminho
# Implementar BFS (Breadth-First Search) de entry até exit
# Retornar o caminho como lista de direções: N, E, S, W
# Usado tanto pelo writer.py (output) quanto pelo renderer.py (exibição)
from mazegen.types import Direction
from typing import List, Tuple
from src.renderer import draw_maze, clear_and_reset
from time import sleep


def solve_bfs(maze) -> List[Tuple]:
    for row in maze.grid:
        for cell in row:
            cell.explored = False
    s_row, s_col = maze.origin
    e_row, e_col = maze.final
    queue = [(s_row, s_col)]
    maze.grid[s_row][s_col].explored = True
    path_map = {(s_row, s_col): None}
    found = False

    while queue:
        curr_r, curr_c = queue.pop(0)
        if (curr_r, curr_c) == (e_row, e_col):
            found = True
            break

        cell = maze.grid[curr_r][curr_c]
        for direction in Direction:
            if cell.walls[direction] is False:
                dr, dc = direction.delta
                nr = curr_r + dr
                nc = curr_c + dc

                if 0 <= nr < maze.height and 0 <= nc < maze.width:
                    neighbor = maze.grid[nr][nc]
                    if not neighbor.explored:
                        neighbor.explored = True
                        path_map[(nr, nc)] = (curr_r, curr_c)
                        queue.append((nr, nc))
    path = []
    if found:
        curr = (e_row, e_col)
        while curr is not None:
            path.append(curr)
            curr = path_map[curr]
        path.reverse()
    else:
        print("Path NOT found!")
    return path


def render_path(canvas, path: List[Tuple], scheme) -> None:
    if not path:
        return
    for i in range(len(path)):
        r, c = path[i]
        cr = 2 * r + 1
        cc = 2 * c + 1

        if canvas[cr][cc] not in [scheme.origin, scheme.exit]:
            canvas[cr][cc] = scheme.solver_path

        if i > 0:
            pr, pc = path[i-1]
            mr = (2 * r + 1 + 2 * pr + 1) // 2
            mc = (2 * c + 1 + 2 * pc + 1) // 2
            if canvas[mr][mc] not in [scheme.origin, scheme.exit]:
                canvas[mr][mc] = scheme.solver_path


def animated_path(canvas, path, scheme):
    for i in range(len(path)):
        r, c = path[i]
        cr = 2 * r + 1
        cc = 2 * c + 1

        if canvas[cr][cc] not in [scheme.origin, scheme.exit]:
            canvas[cr][cc] = scheme.solver_path
        if i > 0:
            pr, pc = path[i-1]
            mr = (2 * r + 1 + 2 * pr + 1) // 2
            mc = (2 * c + 1 + 2 * pc + 1) // 2
            if canvas[mr][mc] not in [scheme.origin, scheme.exit]:
                canvas[mr][mc] = scheme.solver_path
        draw_maze(canvas)
        sleep(0.1)
        if i < len(path) - 1:
            clear_and_reset()
