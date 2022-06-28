# Você deve copiar o seu código do Exercício anterior e realizar algumas modificações.
# Agora no método extrato deverá retornar as operações:
# Exemplo:
#
# conta=Conta("Yasmin", 1, 100)
# conta.saque(50)
# conta.deposito(40)
# conta.saque(9)
# conta.extrato()
# O método extrato() deverá retornar uma extrato bancário (Você deve retornar frases exatamentes como essas, até com os mesmos espaços):
# Operação: Saque    | Valor: R$ 50
# Operação: Depósito | Valor: R$ 40
# Operação: Saque    | Valor: R$ 9
# Saldo Final: R$ 81

# Faça as modificações necessárias nos outros métodos para contemplar o novo extrato.

class Conta():
  listaoperation= []

  def __init__(self,nome,numero_conta,saldo = 0):
    self.nome = str(nome)
    self.numero_conta= int(numero_conta)
    self.saldo=float(saldo)


  def saque(self,retirada_valor):
    if retirada_valor > self.saldo: #se quiser retirar valor menor que meu saldo
      return f"Impossivel, você é pobre "
    elif self.saldo <=0:
      return "Impossivel você não tem dinheiro na conta "
    else:
      self.saldo -=retirada_valor
      Conta.listaoperation.append(f"Operação: Saque    | Valor: {retirada_valor}")
      return f"Você sacou {retirada_valor} agora você tem {self.saldo}"

  def deposito(self,valor_deposito):
    self.saldo +=float(valor_deposito)
    Conta.listaoperation.append(f"Operação: Depósito | Valor: {valor_deposito}")
    return "Operação concluída! ;)"

  def extrato(self):
    for i in Conta.listaoperation:
      print(i +"\n")
    print(f"Saldo Final: {self.saldo} \n")



#Para testar
# conta1=Conta("Yasmin", 1, 100)
# conta2=Conta("Joana", 2, 200)
# conta1.saque(50)
# conta2.deposito(50)
# conta1.saque(10.15)
# conta2.deposito(40)
# conta2.deposito(1000)
# conta1.saque(9)
# conta2.deposito(45.50)
# conta2.saque(250)
