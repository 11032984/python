# Instruções: Escreva um código que retorne a sequência de Fibonacci para uma quantidade de números.
# Para mais informações sobre o que é a Sequência de Fibonacci: https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

# Exemplo 1:
# Quantos números você quer gerar? 5
# [1, 1, 2, 3, 5]
# Exemplo 2:
# Quantos números você quer gerar? 10
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Exemplo 3:
# Quantos números você quer gerar? 0
# []


def fibonacci(num):
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

num = int(input("Quantos números você quer gerar? "))
print(fibonacci(num))
