# Nesse exercícios você deverá criar 3 métodos que irá receber um array de números inteiros e retornar a Média Aritmética Simples deles (https://www.todamateria.com.br/media/).
# O primeiro método você deverá fazer utilizando WHILE, no segundo FOR e no terceiro de alguma outra maneira.

# Exemplo:
# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# print(media_while(lista_numeros)) # 5.5
# print(media_for(lista_numeros)) # 5.5
# print(media(lista_numeros)) # 5.5
from statistics import mean

################################################

def media_while(numeros):
  contador = 0
  soma = 0
  while(contador < len(numeros)):
    soma = soma + numeros[contador] # ou soma += numeros[contador]
    contador += 1
  return soma/len(numeros)
print(media_while([1,2,3,4,5,6,7,8,9,10]))

def media_for(numeros):
  soma = 0
  for numero in numeros:
    soma += numero
  return soma/len(numeros)
print(media_for([1,2,3,4,5,6,7,8,9,10]))

from statistics import mean

def media(numeros):
  return mean(numeros)
print(media([1,2,3,4,5,6,7,8,9,10]))
