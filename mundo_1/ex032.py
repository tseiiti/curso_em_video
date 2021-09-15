from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 032:
Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO.
''')

from datetime import date
n = int(input('Qual é o ano: '))

if n == 0:
  n = date.today().year
  
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
  print('O ano {} é bissexto'.format(n))
else:
  print('O ano {} não é bissexto'.format(n))


