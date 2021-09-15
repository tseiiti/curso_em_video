from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 023:
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados.
Ex:
Digite um número: 1834
unidade:4 dezena:3 centena:8 milhar:1
''')

n = '0000' + str(int(input('Digite um número: ')))
l = len(n)
print('unidade: {}'.format(n[l - 1]))
print('dezena: {}'.format(n[l - 2]))
print('centena: {}'.format(n[l - 3]))
print('milhar: {}'.format(n[l - 4]))
