
class Moto():

  def __init__(self, modelo, cor, ano, hodometro = 200):

   self.modelo = modelo
   self.cor = cor
   self.ano = ano
   self.hodometro = hodometro


  def buzinar (self):
   return f'bi bi'

  def pilotar(self):
   self.hodometro += self.hodometro

  def __str__(self):
    return f' O modelo {self.modelo} de cor {self.cor} do ano {self.ano} tem {self.hodometro} km rodados'

honda_neo = Moto("Honda Neo", "Preto", 2022, 26)
kawasaki = Moto("Kawasaki Ninja", "Verde", 2000, 25)


print(honda_neo)
print(honda_neo.buzinar())
print(kawasaki)
print(kawasaki.buzinar())
kawasaki.pilotar()
honda_neo.pilotar()
print(f"{kawasaki.hodometro} km rodados")
print(f"{honda_neo.hodometro} km rodados")
