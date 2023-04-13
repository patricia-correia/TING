def exists_word(word, instance):
    found = []

    for i in range(len(instance)):
        data = instance.search(i)
        path = data["linhas_do_arquivo"]
        occurrences = []
        for file in range(len(path)):
            if word.lower() in path[file].lower():
                occurrences.append(file + 1)

        if len(occurrences):
            found.append({
                'palavra': word,
                'arquivo': data['nome_do_arquivo'],
                'ocorrencias': [{'linha': line} for line in occurrences]
            })

    return found


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
