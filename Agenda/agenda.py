# TODO: Crie o mini-desafio da agenda mas agora gravando em um arquivo. Instruções: https://youtu.be/Pr--2fMCPrY
# A agenda deverá exibir os contatos gravados, ter a opção de incluir um novo contato e apagar contatos
# Dica 1: Sempre que inicializar a agenda leia todo o arquivo, para obter todos os contatos.
# Dica 2: Você pode gravar no arquivo quando for fechar a agenda ou quando incluir um novo contato.
# IMPORTANTE: Este exercício não tem teste (pytest) por isso use sua criatividade para criar a sua agenda.
from posixpath import split


def remover_contato():
    agenda = open('agenda.txt', 'r')
    agenda_lista = agenda.read().split()
    agenda_dicio = {}

    for nome_num in agenda_lista:

      if agenda_lista.index(nome_num) % 2==0:
         agenda_dicio [nome_num] = agenda_lista[agenda_lista.index(nome_num) +1]

    remover = str(input('Digite o nome para remover: ')).strip()

    if remover in agenda_dicio:
      confirmacao = int(input('Confirma que {} será removido de sua agenda? 1 sim, 2 - não '.format(remover)))

      if confirmacao ==1:

         agenda_dicio.pop(remover)

         for nome, telefone in agenda_dicio.items():
            agenda = open('agenda.txt','w')
            agenda.write('{} {}'.format(nome, telefone))
            agenda.close()
            return menu_agenda()
      elif confirmacao == 2:
       return menu_agenda()
