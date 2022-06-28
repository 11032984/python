
# Nesse exercício você deverá criar alguns métodos para desenho de padrões.
# Dica o método print aceita parâmetros como separador e final de linha (Você poderá usar um).
# Veja mais: https://www.w3schools.com/python/ref_func_print.asp

# Padrão 1:
# padrao1() # Não se esqueça de chamar o método
# 1
# 22
# 333
# 4444
# 55555
def padrao1():

  rows = 5
  for i in range(rows + 1):
    for j in range(i): # Perceba que não é usado a variável j
      print(i, end='')
    print('')

padrao1()



# Padrão 2:
# padrao2()
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def padrao2():
  rows = 5
  for i in range(0, rows):
    for j in range(0, i + 1):
      print("*", end=' ')
    print("\r")

  for i in range(rows, 0, -1):
    for j in range(0, i - 1):
      print("*", end=' ')
    print("\r")

padrao2()


