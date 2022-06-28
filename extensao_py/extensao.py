# TODO: escreva um método que receba um nome de um arquivo com a extensão e retorne a extensão.
# Exemplo:
# print(extensao("teste.py")) -> Irá retornar "A extensão é: py"
# print(extensao("eye_of_the_tiger.mp3")) -> Irá retornar "A extensão é: mp3"

# TODO: crie seu método aqui

def extensao(string):
  return f"A extensao é: {string.split('.')[-1]}"

print(extensao("teste.py"))
print(extensao("eye_of_the_tiger.mp3"))
