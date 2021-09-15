from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 024:
Crie um programa que leia o nome de uma cidade e dita se ela
começa ou não com o nome "SANTO".
''')

n = input('Digite o nome da cidade: ')
print('nome começa com "SANTO": {}'.format('santo' in n.split()[0].lower()))
