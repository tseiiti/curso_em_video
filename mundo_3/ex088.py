from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 088:
Faça um programa que ajude um jogador da MEGA SENA a criar 
palpites. O programa vai perguntar quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando 
tudo em uma lista composta.
''')

from random import randint

lst = []
print('-' * 40)
print(f'{"MEGA SENA":^40}')
print('-' * 40)
n = int(input('Quantos jogos ? '))
for i in range(n):
  l = []
  j = 0
  while j < 6:
    v = randint(1, 60)
    if v not in l:
      l.append(v)
      j += 1
  lst.append(sorted(l))

for i in range(n):
  print(f'Jogo {i + 1}: {[f"{j:02}" for j in lst[i]]}')

