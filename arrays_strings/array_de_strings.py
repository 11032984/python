# Escreva um método que receba uma lista de strings e retorne o tamanho de cada palavra.
# Exemplo:
# print(conta_palavras(["sirius", "python", "segunda-feira", "web", ""]))
# [6, 6, 13, 3, 0]


# TODO crie seu método aqui

def conta_palavras(palavras):
 list1 = []
 for i in palavras:
    list1.append(len(i))
 return list1

list1 = (["sirius", "python", "segunda-feira", "web", ""])
print(conta_palavras(list1))
