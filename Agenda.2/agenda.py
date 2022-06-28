# Nesse exercícios vamos recriar a nossa agenda.
# Intruções:
# 1 - Crie uma classe Agenda, que receba um nome na inicialização Você deverá ter um atributo chamado contatos do tipo dicionário (Hash) para armazenar os contatos.
# 2 - Crie um método chamado adicionar_contato que receba dois parâmetros nome e telefone
# 3 - Crie outro método chamado remover_contato que receba como parâmetro o nome de um contato a ser removido



# TODO: Escreva seu código aqui

from itertools import tee


class Agenda():

    def __init__(self,contatos = {}):
        self.contatos = contatos

    def adicionar_contato(self,nome,telefone):
        self.contatos[nome] = str(telefone)

    def remover_contato(self,nome):
         del self.contatos [nome]

    def exibir_agenda(self):
        for nome, telefone in self.contatos.items():
            print(nome + " : " + telefone)

    def exibir(self):
        for key, velue in self.contatos.items():
            print(self.contatos)



########################
# Para testar:
#agenda = Agenda()
#print(agenda.exibir())
#agenda.adicionar_contato("Tulio", "3333")
#agenda.adicionar_contato("Carol", "3334")
#print(agenda.adicionar_contato("Ana", "1111"))
#print(agenda.exibir())
#agenda.remover_contato("Carol")
#print(agenda.exibir())
