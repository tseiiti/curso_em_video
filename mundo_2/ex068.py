from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 068:
Faça um programa que jogue para ou ímpar com o computador. O 
jogo só será interrompido quando o jogador PERDER, 
mostrando o total de vitórias consecutivas que ele conquistou no 
final do jogo.
''')

from time import sleep
from random import randint

co = 0
mj = -1
us = -1
while True:
  print('\n' + '=-' * 20, end='')
  print('=\n= JOGO DE PAR OU ÍMPAR')
  print('=-' * 20, end='')
  print(f'=\n(partidas vencidas até agora: {co})\n')

  mj = ''
  while not mj or mj not in 'PI':
    mj = input('Escolha entre [P]ar ou [I]mpar: ').strip().upper()[0]
  mj = 0 if mj == 'P' else 1
  print(f'Você escolheu "{"PAR" if mj == 0 else "ÍMPAR"}" então o computador escolhe "{"ÍMPAR" if mj == 0 else "PAR"}"!')

  pc = randint(0, 5)
  print('computador pensando', end= '')
  for i in range(3):
    print('.', end= '')
    sleep(0.5)
  print('\n... o computador já pensou na jogada')

  while us not in range(0, 6):
    us = int(input('Escolha a sua jogada (0 a 5 dedos): '))

  print('')
  msg = f'\nO computador jogou {pc} e você {us}. Total {pc + us} é {"PAR" if (pc + us) % 2 == 0 else "ÍMPAR"}'
  if (pc + us) % 2 == mj:
    print('*' * 20)
    print('*** Você GANHOU!')
    print('*' * 20)
    print(f'{msg}')
  else:
    print('-' * 20)
    print('Você PERDEU!')
    print(f'{msg}')
    break

  co += 1
  mj = -1
  us = -1

print(f'Você ganhou {co} jogadas')