from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 029:
Escreva um programa que leia a velociade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
''')

n = float(input('Informe sua velocidade: '))

if n > 80:
  print('Você foi multado em R$ {:.2f}!'.format((n - 80) * 7))
