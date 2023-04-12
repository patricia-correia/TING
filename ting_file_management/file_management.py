import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido')

    try:
        with open(path_file) as path:
            return path.read().split('\n')

    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
