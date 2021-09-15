from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 009:
Faça um programa que leia um número inteiro qualquer e mostre na
tela a sua tabuada.
''')

n = int(input('Digite um número: '))
print('{} X  1 = {:2}'.format(n, n * 1))
print('{} X  2 = {:2}'.format(n, n * 2))
print('{} X  3 = {:2}'.format(n, n * 3))
print('{} X  4 = {:2}'.format(n, n * 4))
print('{} X  5 = {:2}'.format(n, n * 5))
print('{} X  6 = {:2}'.format(n, n * 6))
print('{} X  7 = {:2}'.format(n, n * 7))
print('{} X  8 = {:2}'.format(n, n * 8))
print('{} X  9 = {:2}'.format(n, n * 9))
print('{} X 10 = {:2}'.format(n, n * 10))
