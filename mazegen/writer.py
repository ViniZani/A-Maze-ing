# escreve no txt os dados
# 1) labiritnto em hexa \n
# 2) entrada \n saida \n
# 3) melhor path em coordenadas
import os


def write_hex_path():
    """Escreve o maze em hexadecimal no arquivo"""
    pass


def write_data(origin_x, origin_y, final_x, final_y):
    content = f"{origin_x},{origin_y}\n{final_x}, {final_y}\n"
    with open(os.getenv('OUTPUT_FILE'), 'w', encoding='utf-8') as arquivo:
        arquivo.write(content)


def write_cord_path():
    """Escreve as corrdenaadas do melhor path no arquivo"""
    pass
