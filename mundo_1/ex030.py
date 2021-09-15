from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 030:
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.
''')

n = int(input('Informe um número inteiro: '))

if n % 2 == 0:
  print('O número é PAR')
else:
  print('O número é ÍMPAR')
