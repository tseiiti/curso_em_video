from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 054:
Crie um programa que leia o ano de 
nascimento de sete pessoas. No 
final, mostre quantas pessoas 
ainda não atingiram a maioridade e 
quantas já são maiores.
''')

from datetime import date
ano = date.today().year

t = 0
for i in range(7):
  n = int(input('Digite o ano de nascimento: '))
  if ano - n < 21:
    t += 1

print('{} pessoas são maiores'.format(7 - t))
print('{} pessoas não são maiores'.format(t))
