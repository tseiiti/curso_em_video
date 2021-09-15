from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 019:
Um professor quer sortear um dos seus quatro alunos para apagar
o quadro. Faça um um programa que ajude ele, lendo o nome deles e
escrevendo o nome escolhido.
''')

from random import choice

alunos = []
alunos.append(input('Digite o nome do primeiro aluno: '))
alunos.append(input('Digite o nome do segundo aluno: '))
alunos.append(input('Digite o nome do terceiro aluno: '))
alunos.append(input('Digite o nome do quarto aluno: '))

print('O aluno escolhido é {}'.format(choice(alunos)))
