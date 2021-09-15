from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 031:
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais logas.
''')

n = float(input('Qual a distância em km: '))

if n <= 200:
  print('O preço é R$ {:.2f}'.format(n * 0.5))
else:
  print('O preço é R$ {:.2f}'.format(n * 0.45))
