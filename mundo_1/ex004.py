from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 004:
Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele.
''')

x = input('Digite algo:')
print('o tipo é: {}'.format(type(x)))
print('é alfanumérico: {}'.format(x.isalnum()))
print('é alfabético: {}'.format(x.isalpha()))
print('é numérico: {}'.format(x.isnumeric()))
print('é maiúsculo: {}'.format(x.isupper()))
print('é dígito: {}'.format(x.isdigit()))
print('é decimal: {}'.format(x.isdecimal()))
print('é identificador: {}'.format(x.isidentifier()))
print('é minúsculo: {}'.format(x.islower()))
print('é imprimível: {}'.format(x.isprintable()))
print('é espaço: {}'.format(x.isspace()))
print('é capitalizado: {}'.format(x.istitle()))
