# TODO: Crie um método que irá ler o arquivo "pares.txt" e irá salvar no arquivo "multiplos.txt" todos os múltiplos de 3, um número por linha.
# IMPORTANTE: Este exercício não tem teste (pytest).

def leitura_escrita_arquivo():

    pares = open('pares.txt', 'r')
    num_pares = pares.read().split()

    multiplos = open('multiplos.txt', 'a')
    for num in num_pares:
        num = int(num)
        if num % 3 == 0:
           multiplos.write('{}, '.format(num))
        else:
            continue

    multiplos.close()

leitura_escrita_arquivo()
