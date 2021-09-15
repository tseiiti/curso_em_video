from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 034:
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superioresz a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
''')

n = float(input('Qual é o salário: R$ '))

if n > 1250:
  print('o novo salario é R$ {:.2f}'.format(n * 1.1))
else:
  print('o novo salario é R$ {:.2f}'.format(n * 1.15))
