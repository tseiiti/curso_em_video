from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 038:
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
''')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
  print('O primeiro valor é maior')
elif n1 < n2:
  print('O segundo valor é maior')
else:
  print('Não existe valor maior, os dois são iguais')
