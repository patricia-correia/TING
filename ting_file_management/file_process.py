import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)

    output = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file
    }

    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    instance.enqueue(output)
    return sys.stdout.write(str(output))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write('Não há elementos\n')

    delete = instance.dequeue()['nome_do_arquivo']

    return sys.stdout.write(f'Arquivo {delete} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        response = instance.search(position)
        return sys.stdout.write(str(response))

    except IndexError:
        return sys.stderr.write('Posição inválida')
