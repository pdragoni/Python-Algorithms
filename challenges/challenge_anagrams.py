def sort_string(string):
    list_string = list(string)
    # transforma a string em uma lista de caracteres

    for a in range(len(list_string)):
        for b in range(a + 1, len(list_string)):
            if list_string[a] > list_string[b]:
                list_string[a], list_string[b] = list_string[b], list_string[a]
    # ordena a lista de caracteres sem usar sort ou sorted
    return "".join(list_string)
    # retorna a lista de caracteres como uma string


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    raise NotImplementedError
