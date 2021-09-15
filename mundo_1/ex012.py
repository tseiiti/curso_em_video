from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 012:
Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
''')

n = float(input('Digite o preço do produto: R$ '))
print('o preço com 5% de desconto é: R$ {:.2f}'.format(n * 0.95))
