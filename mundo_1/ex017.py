from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 017:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
''')

from math import hypot

n1 = float(input('Cateto oposto: '))
n2 = float(input('Cateto adjacente: '))
#print('A hipotenusa é {}'.format((n1 ** 2 + n2 ** 2) ** 0.5))
print('A hipotenusa é {}'.format(hypot(n1, n2)))
