
from loteria import Loteria

loteria = Loteria #instanciando um objeto do tipo Loteria

meus_numeros = [4, 12, 17, 32, 47, 59]
numeros_sorteados = 0
sorteando = True

while (sorteando):
    numeros_sorteados +=1
    if sorteando == loteria.sorteio():
      sorteando = False
    if numeros_sorteados > 100000:
      break
print(numeros_sorteados)
