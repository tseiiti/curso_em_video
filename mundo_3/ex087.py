from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 087:
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
''')

lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a = b = c = 0
for i in range(3):
  for j in range(3):
    n = int(input(f'Digite o valor[{i}][{j}]: '))
    lst[i][j] = n

    # soma dos valores pares
    if n % 2 == 0:
      a += n

    # soma da 3a coluna
    if j == 2:
      b += n

    # maior valor da segunda linha
    if i == 1 and (j == 0 or n > c):
      c = n

print('=-' * 20 + '=')
for i in range(3):
  print(f'[{lst[i][0]:^5}] [{lst[i][1]:^5}] [{lst[i][2]:^5}]')

print(f'A) A soma de todos os valores pares digitados: {a}')
print(f'B) A soma dos valores da terceira coluna: {b}')
print(f'C) O maior valor da segunda linha: {c}')
