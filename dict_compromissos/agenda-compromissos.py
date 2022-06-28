# Nesse exercício você deverá criar uma agenda simplificada de um consultório.
# Cada horário poderá ser ocupado por uma pessoa.

# Veja o funcionamento esperado aqui: https://d.pr/v/XfBLL2


AGENDA = {
  '8': 'vazio',
  '9': 'vazio',
  '10': 'vazio',
  '11': 'vazio',
  '13': 'vazio',
  '14': 'vazio',
  '15': 'vazio',
  '16': 'vazio'
}

# EXTRA
# Como funcionalidades extras você pode adicionar:
# - Não deixar adicionar pessoas em horários não permitidos pela agenda.
# - Transforme a string do nome do Paciente em um objeto da classe Paciente (Você precisará cria-la) com os atributos: nome, telefone, data de nascimento. Exiba esses dados no método de exibir agenda
# - Transforme a agenda em uma classe

# TODO: escreva seus métodos e menu aqui

def exibir_agenda():
  print('\n')
  for horario in AGENDA:
    print("Horário: " + horario + " - Paciente: " + AGENDA[horario])

def adicionar_paciente():
  horario = input("Qual o horario? ")
  nome = input("Qual o nome? ")
  AGENDA[horario] = nome

def remover_paciente():
  horario = input("Qual o horário para remover? ")
  AGENDA[horario] = 'vazio'

sair = False
while(sair == False):
  print('\n-----------------------------')
  print('Acessar agenda')
  print('Escolha uma opção:')
  print('1. Exibir agenda')
  print('2. Adicionar adicionar um(a) paciente')
  print('3. Remover um(a) paciente')
  print('4. Sair')
  opcao = int(input("> "))

  if opcao == 1:
    exibir_agenda()
  elif opcao == 2:
    adicionar_paciente()
  elif opcao == 3:
    remover_paciente()
  elif opcao == 4:
    sair = True
  else:
    print('**** opção não encontrada ****')

print('Agenda fechada')
