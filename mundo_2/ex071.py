from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 071:
Crie um programa que simule o funcionamento de um 
caixa eletrônico. No início, pergunte ao usuário qual será o 
valor a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
''')

valor = float(input('Que valor você quer sacar: R$ '))
t50 = 0
t20 = 0
t10 = 0
t01 = 0
while valor > 0:
  if valor >= 50:
    valor -= 50
    t50 += 1
  elif valor >= 20:
    valor -= 20
    t20 += 1
  elif valor >= 10:
    valor -= 10
    t10 += 1
  else:
    valor -= 1
    t01 += 1

print(f'Total de cédulas de R$ 50,00: {t50}')
print(f'Total de cédulas de R$ 20,00: {t20}')
print(f'Total de cédulas de R$ 10,00: {t10}')
print(f'Total de cédulas de R$ 1,00: {t01}')
