def count_vowels(string):
    # TODO: a função deve retornar a quantidade de vogais em string
    # Dica: use loop for e condicionais
    # Exemplo: string = 'qualquer texto' deve retornar 6

    string = string.lower()
    nA = (string.count('a'))
    nE = (string.count('e'))
    nI = (string.count('i'))
    nO = (string.count('o'))
    nU = (string.count('u'))


    return nA + nE + nI + nO + nU
print(count_vowels('qualquer texto'))
