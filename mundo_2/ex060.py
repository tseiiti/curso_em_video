from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 060:
Faça um programa que leia um número 
qualquer e mostrew o seu fatorial.
Ex:
5!=5x4x3x2x1=120
''')

n = int(input('Digite um número: '))
i = n
f = 1
print('{}! ='.format(n), end='')
while i > 1:
  print(' {} x'.format(i), end='')
  f *= i
  i -= 1

print(' 1 = {}'.format(f))
