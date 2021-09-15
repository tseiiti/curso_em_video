from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 037:
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
''')

n = int(input('Digite um número: '))
print('1: binário')
print('2: octal')
print('3: hexadecimal')
c = int(input('Qual base para conversão: '))

if c == 1:
  print('em binário: {}'.format(bin(n).upper()))
elif c == 2:
  print('em octal: {}'.format(oct(n).upper()))
elif c == 3:
  print('em hexadecimal: {}'.format(hex(n).upper()))
