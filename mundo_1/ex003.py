from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 003:
Crie um programa que leia dois números e mostre a soma entre eles.
''')

n1 = int(input('primeiro número:'))
n2 = int(input('segundo número:'))
print('a soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
