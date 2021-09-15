from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 022:
Crie um programa que leia o nome completo de uma pessoa e
mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
''')

nome = input('Digite seu nome completo: ')
print('Letras maiúscula: {}'.format(nome.upper()))
print('Letras minúscula: {}'.format(nome.lower()))
print('Tamanho: {} letras'.format(len(nome) - nome.count(' ')))
print('Tamanho do nome: {} letras'.format(len(nome.split()[0])))
