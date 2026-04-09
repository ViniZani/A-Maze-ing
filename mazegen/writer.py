# escreve no txt os dados
# 1) labiritnto em hexa \n
# 2) entrada \n saida \n
# 3) melhor path em coordenadas
import os


def write_hex_path(grid, height, width):
    """Escreve o maze em hexadecimal no arquivo"""
    with open(os.getenv('OUTPUT_FILE'), 'w', encoding='utf-8') as archive:
        for i in range(height):
            for j in range(width):
                archive.write(f"{grid[i][j]:X}")
            archive.write("\n")


def write_data(origin_x, origin_y, final_x, final_y):
    content = f"\n{origin_x},{origin_y}\n{final_x}, {final_y}\n"
    with open(os.getenv('OUTPUT_FILE'), 'a', encoding='utf-8') as archive:
        archive.write(content)


def write_cord_path():
    """Escreve as corrdenaadas do melhor path no arquivo"""
    coord_path = "SWESWENSEWNNEESSWENNWEE"
    with open(os.getenv('OUTPUT_FILE'), 'a', encoding='utf-8') as archive:
        archive.write(coord_path)
        archive.write("\n")
