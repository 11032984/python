# TODO: Crie um método que irá gravar os números de 0 a 100 em dois arquivos, no arquivo "impares.txt" grave os números ímpares e
# no arquivo "pares.txt" grave os números pares.
# IMPORTANTE: Este exercício não tem teste (pytest).


def escrever_pares_impares():

     pares = open('pares.txt', 'a')
     impares = open('impares.txt','a')

     for numero  in range(101):
         if numero %2 >=1:
           impares.write("{}".format(numero))
         else:
           pares.write("{}".format(numero))

     pares.close()
     impares.close()

escrever_pares_impares()
