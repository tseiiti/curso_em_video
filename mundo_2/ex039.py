from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 039:
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
''')

from datetime import date

n = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - n

print('Você tem {} anos'.format(idade))

if idade < 18:
  print('Ainda vai se alistar')
  print('Falta {} anos'.format(18 - idade))
elif idade == 18:
  print('Hora de se alistar')
else:
  print('Já passou do tempo')
  print('Passou {} anos'.format(idade - 18))
