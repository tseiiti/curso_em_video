from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 084:
Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Um listagem com as pessoas mais leves.
''')

lst = []
m = 0
l = 0
while True:
  n = input('Digite o nome: ')
  p = float(input('Digite o peso: '))
  
  if m < p or len(lst) == 0:
    m = p

  if l > p or len(lst) == 0:
    l = p

  lst.append([n, p])

  r = input('Continua (S/N) ?')
  if r and r in 'Nn':
    break

print('+-' * 20 + '=')
print(f'A) Foram cadastradas {len(lst)} pessoas')
print(f'B) As pessoas mais pesadas são: {[p[0] for p in lst if p[1] == m]}')
print(f'C) As pessoas mais leves são: {[p[0] for p in lst if p[1] == l]}')
