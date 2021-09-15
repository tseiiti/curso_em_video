from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 016:
Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
''')

#from math import trunc

n = float(input('Digite um número decimal: '))
#print('A parte inteira do número {} é {}'.format(n, trunc(n)))
print('A parte inteira do número {} é {}'.format(n, int(n)))
