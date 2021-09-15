from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 008:
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.
km hm dam m dm cm mm
''')

n = float(input('Digite um número em metros: '))
print('o valor em centímetros é: {}cm'.format(n * 100))
print('o valor em milímetros é: {}mm'.format(n * 1000))
