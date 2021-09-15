from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 041:
A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
''')

from datetime import date

n = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - n

print('Você tem {} anos'.format(idade))

if idade < 9:
  print('MIRIM')
elif idade < 14:
  print('INFANTIL')
elif idade < 19:
  print('JUNIOR')
elif idade < 20:
  print('SÊNIOR')
else:
  print('MASTER')
