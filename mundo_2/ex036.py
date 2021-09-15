from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 036:
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o
empréstimo será negado.
''')

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário: '))
anos = float(input('Informe quantos anos: '))

prestacao = valor_casa / (anos * 12)

if prestacao > salario * 0.3:
  s = 'Empréstimo negado. O valor da prestação é '
else:
  s = 'Empréstimo aprovado. O valor da prestação é '

print('{}R$ {:.2f} ({:.2f}% de seu salário)'.format(s, prestacao, prestacao / salario * 100))
