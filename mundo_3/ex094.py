from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 094:
Crie um programa que leia nome, sexo e idade de várias 
pessoas, guardando os dados de cada pessoa em um 
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
''')

lst = []
dct = {}
t = 0
while True:
  dct['nome'] = input('Nome: ')
  dct['sexo'] = ''
  while not dct['sexo'] or dct['sexo'] not in 'MF':
    dct['sexo'] = input('Sexo (M/F): ').strip()[0].upper()
  dct['idade'] = int(input('Idade: '))
  lst.append(dct.copy())
  t += dct['idade']

  r = input('Continua (S/N) ?')
  if r and r in 'Nn':
    break
b = t / len(lst)

c = []
d = []
for dct in lst:
  if dct['sexo'].upper() == 'F':
    c.append(dct['nome'])

  if dct['idade'] > b:
    d.append(dct['nome'])

print(f'A) Quantas pessoas foram cadastradas: {len(lst)}')
print(f'B) A média de idade do grupo: {b}')
print(f'C) Uma lista com todas as mulheres: {c}')
print(f'D) Uma lista com todas as pessoas com idade acima da média: {d}')
