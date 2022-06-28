# Nesse exercícios você deverá criar 3 métodos que irá receber um array de números inteiros e retornar a soma deles.
# O primeiro método você deverá fazer utilizando WHILE, no segundo FOR e no terceiro de alguma outra maneira.

# Exemplo:
# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# print(soma_while(lista_numeros)) # 55
# print(soma_for(lista_numeros)) # 55
# print(soma(lista_numeros)) # 55

def soma_while(numeros):
  contador = 0
  soma = 0
  while(contador < len(numeros)):
    soma = soma + numeros[contador] # ou soma += numeros[contador]
    contador += 1
  return soma
print(soma_while([1,2,3,4,5,6,7,8,9,10]))


def soma_for(numeros):
  soma = 0
  for numero in numeros:
    soma += numero
  return soma
print(soma_for([1,2,3,4,5,6,7,8,9,10]))


def soma(numeros):
  return sum(numeros)

print(soma([1,2,3,4,5,6,7,8,9,10]))
