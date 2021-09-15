from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 013:
Faça um algoritmo que leia o salário de um funcionário e mostre seu
novo salário, com 15% de aumento.
''')

n = float(input('Digite o salário atual: R$ '))
print('o novo salário com 15% de aumento é: R$ {:.2f}'.format(n * 1.15))
