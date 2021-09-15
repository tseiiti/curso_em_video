from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 020:
O mesmo professor do desafio anterior quer sortear a orde de
apresentação de trabalhos dos alunos. Faça um programa que leia
o nome dos quatro alunos e mostre a ordem sorteada.
''')

from random import shuffle

alunos = []
alunos.append(input('Digite o nome do primeiro aluno: '))
alunos.append(input('Digite o nome do segundo aluno: '))
alunos.append(input('Digite o nome do terceiro aluno: '))
alunos.append(input('Digite o nome do quarto aluno: '))
#alunos.sort()
shuffle(alunos)
print('O alunos sorteados é {}'.format(alunos))
