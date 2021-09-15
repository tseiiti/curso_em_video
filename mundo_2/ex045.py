from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 045:
Crie um programa que faça o 
computador jogar Jokenpô
com você.
''')

from random import randint

print('1 = pedra')
print('2 = papel')
print('3 = tesoura')
us = int(input('Escolha sua jogada: '))
pc = randint(1, 3)

j = ['', 'pedra', 'papel', 'tesoura']
print('Você escolheu {}'.format(j[us]))
print('O computador escolheu {}'.format(j[pc]))

if pc == us:
  print('Empatou')
elif str(pc) + str(us) in ('12', '23', '31'):
  print('Você ganhou')
else:
  print('Você perdeu')
