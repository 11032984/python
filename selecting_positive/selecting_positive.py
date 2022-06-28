import numbers

def selecting_positive(list1, number):
    # TODO: a função deve retornar uma nova lista apenas com os valores maiores que o number
    # Exemplo: list1 = [10,20,30,40,50] e number = 20, a função deve retornar [30,40,50]
    # Dica: use laço de repetição e condicionais

    nova_list =[]
    for x in list1:
        if x > number:
         nova_list.append(x)
    return (nova_list)
