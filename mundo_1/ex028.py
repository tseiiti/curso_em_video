from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 028:
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.
''')

from random import randint
from time import sleep
n1 = randint(0, 5)
n2 = int(input('Adivinhe em um número entre 0 e 5: '))
sleep(3)

if n1 == n2:
  print('Você venceu!')
else:
  print('Você perdeu, o número correto era {}'.format(n1))
