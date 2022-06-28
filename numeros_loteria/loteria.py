import random

class Loteria():

   def sorteio():
     numeros = range(1,60,1)
     sorteados = random.sample(numeros,6)
     sorteados.sort()
     return sorteados

