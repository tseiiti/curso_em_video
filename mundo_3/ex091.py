from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 091:
Crie um programa onde 4 jogadores joguem um dado e 
tenham resultados aleatórios. Guarde esses resultados em 
um dicionário. No final, coloque esse dicionário em ordem, 
sabendo que o vendedor tirou o maior número no dado.
''')

from random import randint
from time import sleep
from operator import itemgetter

dct = {}
for i in range(4):
  id = 'jogador_' + str(i + 1)
  vlr = randint(1, 6)
  dct[id] = vlr
  print(f'O {id} tirou {vlr}')
  sleep(1)

# print(dct)
print('=-' * 20 + '=')
print(f'{"== Ranking dos jogadores! ==".upper():^41}')
# valores = list(set(dct.values()))
# valores.sort(reverse=True)
# c = 1
# for vlr in valores:
#   for i, v in dct.items():
#     if vlr == v:
#       print(f'\t{c}° lugar: {i} com {v}')
#       c += 1
#       sleep(1)

dct = sorted(dct.items(), key= itemgetter(1), reverse= True)
for i in range(len(dct)):
  print(f'\t{i + 1}° lugar: {dct[i][0]} com {dct[i][1]}')
  sleep(1)

