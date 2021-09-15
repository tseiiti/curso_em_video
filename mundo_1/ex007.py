from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 007:
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
''')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('a média é: {}'.format((n1 + n2) / 2))
