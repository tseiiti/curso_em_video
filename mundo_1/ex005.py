from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 005:
Faça um programa que leia um número inteiro e mostre na tela o seu
sucessor e o seu antecessor.
''')

n = int(input('Digite um número: '))
print('Analisando o número {}, o seu antecessor é {} e o sucessor é {}'.format(n, n - 1, n + 1))
