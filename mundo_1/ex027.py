from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 027:
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
''')

n = input('Digite seu nome completo: ')
print('seu primeiro nome: {}'.format(n.split()[0]))
print('seu último nome: {}'.format(n.split()[-1]))
