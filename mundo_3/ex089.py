from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 089:
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um 
boletim contendo a média de cada um e permita que o usuário 
possa mostrar as notas de cada aluno individualmente.
''')

lst = []
while True:
  # aluno = []
  # notas = []
  # aluno.append(input('Nome: '))
  # notas.append(float(input('Nota 1: ')))
  # notas.append(float(input('Nota 2: ')))
  # aluno.append(notas.copy())
  # lst.append(aluno.copy())
  nom = input('Nome: ')
  n1 = float(input('Nota 1: '))
  n2 = float(input('Nota 2: '))
  lst.append([nom, [n1, n2]])

  r = input('Continua (S/N) ?')
  if r and r in 'Nn':
    break

print('=-' * 20 + '=')
print(f'N°. NOME                MÉDIA')
print('-' * 41)
for i in lst:
  print(f'{lst.index(i):<4}{i[0].title():20}{sum(i[1]) / 2:>5}')
print('-' * 41)

i = 0
while i != 999:
  i = int(input('Qual aluno (999 interrompe)? '))
  if i in range(len(lst)):
    print(f'Notas de {lst[i][0]} são: {lst[i][1]}')