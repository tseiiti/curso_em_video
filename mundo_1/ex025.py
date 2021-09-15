from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 025:
Crie um programa que leia o nome de uma pessoa e diga se ela tem
"SILVA" no nome.
''')

n = input('Digite seu nome: ')
print('nome tem "SILVA": {}'.format('silva' in n.lower()))
