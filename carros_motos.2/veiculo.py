from moto import Moto
from carro import Carro


class Veiculo(Moto, Carro):
   def __init__(self, modelo, cor, ano, hodometro = 2000):
      super().__init__(modelo, cor, ano, hodometro)
