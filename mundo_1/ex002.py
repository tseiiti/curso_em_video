from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 002:
Faça um programa que leia o nome de uma pessoa e mostre uma
mensagem de boas-vindas.
''')

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))
