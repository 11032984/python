# Você deverá criar uma classe chamada Conta, essa classe irá simular de forma simples o funcionamento de
# uma conta bancária.
# Essa conta devera ter atributos nome_cliente, numero_conta e saldo. Ao criar uma conta o saldo deverá ser 0.
# Você deverá fazer 3 métodos:
# 1 - extrato - nesse método você exibirá apenas o saldo.
# 2 - saque - Implemente a operação de saque, que irá receber um valor a ser retirado da conta.
# 3 - deposito - Implemente a operação de depósito, que irá receber um valor a ser depositado na conta.



# TODO: Criei seu código

class Conta():

    def __init__(self,nome, numero_conta, saldo = 0):
      self.nome = nome
      self.numero_conta = numero_conta
      self.saldo = saldo

    def extrato(self):
       return "O saldo da conta é " + str(self.saldo)

    def deposito(self,valor_deposito):
         self.saldo += valor_deposito

    def saque(self,retirada_valor):
        if self.saldo >= retirada_valor:
          self.saldo -= retirada_valor
        else:
          print("Saldo insuficiente")


# Para testar
#####################################

#conta1=Conta("Yasmin", 1, saldo = 100)
#print(conta1.extrato())
#conta1.saque(50)                 #yasmin tinha 100 e sacou 50, automaticamente diminiu 50,
#print(conta1.extrato())          # oq lhe restou 50 reias

#####################################
#conta2=Conta("Joana", 2, saldo = 200)
#print(conta2.extrato())              #joana tinha 200 e depositou +50,
#conta2.deposito(50)                   #o que lhe restou foi 250
#print(conta2.extrato())

#####################################
#conta3=Conta('Maria', 3, saldo = 9.0)
#print(conta3.extrato())
#conta3.saque(10.15)            #saldo insuficiente, pois meu saldo e menor que o valor
#print(conta3.extrato())         #que eu quero sacar
#############################
#conta2.deposito(40)
#conta2.deposito(1000)
#conta1.saque(9)
#conta2.deposito(45.50)
#conta2.saque(250)

