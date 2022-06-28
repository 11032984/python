from itertools import count


def approved_alunes():
    # TODO: use o dicionário abaixo para criar uma função que retorne a quantidade de alunes aprovados
    # Considere que a média é 70
    # Dica: use laço de repetição e condicionais
    alunes = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}
    count = 0
    for valor in alunes.values():
           if valor >= (70):
               count +=1
    return count

print(approved_alunes())



def approved_alunes_names():
    # TODO: use o dicionário abaixo para criar uma função que retorne a quantidade de alunes aprovados
    # Considere que a média é 70
    # Dica: use laço de repetição e condicionais
    alunes = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}

    lista = []
    for nome, nota in alunes.items():
           if nota >= (70):
               lista.append(nome)

    return lista
print(approved_alunes_names())


def count_letters(string):
    # TODO: crie uma função que conte quantas vezes cada letra aparece na string e
    # retorne um dicionário com a letra como chave e a quantidade como valor
    # Exemplo: string = 'textooo' deve retornar {'e':1, 't':2, 'x':1, 'o':3}
    # Dica: use laço de repetição, condicionais e seus conhecimentos sobre dicionários

    my_dict={}
    for letras in string:
        if letras not in my_dict.keys():
            my_dict[letras] = 1
        else:
            my_dict[letras] +=1
    return my_dict

print(count_letters('textooo'))
