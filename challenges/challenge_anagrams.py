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
    # inicializa a variável anagram como False
    anagram = False

    # Passa as strings para caracteres minúsculos e para a função de sort
    lowered_first = first_string.lower()
    sorted_first = sort_string(lowered_first)

    lowered_second = second_string.lower()
    sorted_second = sort_string(lowered_second)

    # A validação da igualdade entre as strings ordenadas é atribuída a anagram
    anagram = sorted_first == sorted_second

    # Se uma das strings for vazia, não tem como ser um anagrama
    if sorted_first == "" or sorted_second == "":
        anagram = False

    return (sorted_first, sorted_second, anagram)
