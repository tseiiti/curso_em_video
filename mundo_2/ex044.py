from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 044:
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
''')

n = float(input('Digite o valor do produto: '))
print('1: à vista dinheiro/cheque')
print('2: à vista no cartão')
print('3: em 2 vezes no cartão')
print('4: em 3 vezes ou mais no cartão')
c = int(input('Qual base para conversão: '))

if c == 1:
  print('valor calculado é: R$ {}'.format(n * 0.9))
elif c == 2:
  print('valor calculado é: R$ {}'.format(n * 0.95))
elif c == 3:
  print('valor calculado é: R$ {}'.format(n))
else:
  print('valor calculado é: R$ {}'.format(n * 1.2))
