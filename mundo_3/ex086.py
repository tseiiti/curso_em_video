from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 086:
Crie um programa que crie uma matriz de dimensão 3x3 e 
prencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
''')

lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
  for j in range(3):
    lst[i][j] = input(f'Digite o valor[{i}][{j}]: ')

print('=-' * 20 + '=')
for i in range(3):
  print(f'[{lst[i][0]:^5}] [{lst[i][1]:^5}] [{lst[i][2]:^5}]')
