from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 035:
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou
não formar um triângulo.
''')

n = []
n.append(float(input('Informe a reta 1: ')))
n.append(float(input('Informe a reta 2: ')))
n.append(float(input('Informe a reta 3: ')))
n.sort()

if n[0] + n[1] > n[2]:
  print('forma um triângulo')
else:
  print('não forma um triângulo')
