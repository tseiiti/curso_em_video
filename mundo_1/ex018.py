from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 017:
Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do senom, cosseno e
tangente desse ângulo.
''')

from math import radians, sin, cos, tan

n = float(input('Informe o ângulo: '))
r = radians(n)
s = sin(r)
c = cos(r)
t = tan(r)

print('O seno de {:.1f} graus é {:.2f}.'.format(n, s))
print('O cosseno de {:.1f} graus é {:.2f}.'.format(n, c))
print('A tangente de {:.1f} graus é {:.2f}.'.format(n, t))
