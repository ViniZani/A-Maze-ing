import os


try:
    from dotenv import load_dotenv
except ImportError:
    print("lib dotenv isnt installed, please run: \
    python -m pip install python-dotenv")

load_dotenv(dotenv_path='config.txt')
width = int(os.getenv('WIDTH'))
height = int(os.getenv('HEIGHT'))
grid = [['#' for _ in range(width)] for _ in range(height)]

origin = tuple(map(int, os.getenv('ENTRY').split(',')))
final = tuple(map(int, os.getenv('EXIT').split(',')))
print(f"width: {width}")
print(f"heigth: {height}")
print(f"origin: {origin}")
print(f"final: {final}")


def draw_cell(grid, x, y, char):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        grid[y][x] = char


def render(grid):
    for line in grid:
        print(" ".join(line))


if __name__ == "__main__":
    # Estruturar o projeto

    """Geração do maze"""
    # falta gerar o maze com paredes
    # falta gerar o maze fechado (com as bordas)
    # falta gerar o maze com a lib visual
    # falta colocar o 42 no meio do maze
    draw_cell(grid, origin[0], origin[1], char='E')
    draw_cell(grid, final[0], final[1], char='S')
    render(grid)

    """ Visualização do maze"""
# regerar um novo maze
# mudar cores da wall do maze.
# falta exibir e esconder o melhor caminho possivel do maze
# opcional: falta criar o menu de interação via terminal

    """Envio dos outputs do maze"""
# após tudo, envia os outputs para o .txt
# falta enviar o maze em hexa + \n
# falta enviar as coord do melhor caminho
    content = f"{origin[0]},{origin[1]}\n{final[0]}, {final[1]}\n"
    with open(os.getenv('OUTPUT_FILE'), 'w', encoding='utf-8') as arquivo:
        arquivo.write(content)
