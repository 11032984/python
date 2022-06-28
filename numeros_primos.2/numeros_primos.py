# Ler um número e gerar todos os números primos menores que o número fornecido retornando uma lista com todos eles.
# Sobre números primos
# exemplos:
# prime_numbers(10) -> [2,3,5,7]
# prime_numbers(13) -> [2,3,5,7,11]

from os import remove
import re

def prime_numbers(number):

   nova_list = list(range(2,number))

   for P in range(2,int(number)):
     if P in nova_list:
       for N in range (P**2,number, P):
         if N in nova_list: nova_list.remove(N)

   return nova_list


print(prime_numbers(30))

