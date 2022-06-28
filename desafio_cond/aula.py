def can_vote(age):
  # Melhorar função can_vote já implementada em 02-if/01-posso-votar/my_vote.py
  # TODO: Sendo informado a idade retorne a informação se a pessoa poderá votar seguindo as regras:
  # Menores de 0 anos = "Idade inexistente"
  # Menores de 16 anos = "Não pode votar"
  # Entre 16 e 17 anos = "Podem votar mas não são obrigados"
  # Entre 18 e 70 anos = "Obrigados a votar"
  # Maiores de 70 anos = "Podem votar mas não são obrigados"

  if age < 0:
    return "Idade inexistente"
  elif age < 16:
    return "Não pode votar"
  elif 16 <= age <= 17:
    return "Podem votar mas não são obrigados"
  elif 18 <= age <= 70:
    return "Obrigados a votar"
  else:
    return "Podem votar mas não são obrigados"

  pass


def valid_password(password):
  # TODO: Verifique se a senha (password) é válida e retorne 'Válida' ou 'Não válida' conforme as regras:
  # Somente senhas com tamanho mínimo de 6 e máximo de 16 caracteres

  if 6 <= len(password)<= 16:
    return 'Válida'
  else:
    return 'Não válida'

  pass



def vowel_count(string):
  # TODO: Conte o número de vogais existentes na string passada como parâmetro.
  # Exemplo 1: string = 'Olá Mundo' return = 4
  # Exemplo 2: string = 'Sirius Education' return = 8

  string = string.lower()
  nA = (string.count('a'))
  nE = (string.count('e'))
  nI = (string.count('i'))
  nO = (string.count('o'))
  nU = (string.count('u'))

  return nA + nE + nI + nO + nU

  pass



