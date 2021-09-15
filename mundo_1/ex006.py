from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 006:
Faça um algoritmo que leia um número e mostre na tela o seu dobro, triplo e
raiz quadrada.
''')

n = float(input('Digite um número: '))
print('o dobro é: {}'.format(n * 2))
print('o triplo é: {}'.format(n * 3))
print('a raiz é: {:.2f}'.format(n ** 0.5))
