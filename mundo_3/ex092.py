from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 092:
Crie um programa que leia nome, ano de nascimento e carteira 
de trabalho e cadastre-os (com idade) em um dicionário 
se por acaso a CTPS for diferente de ZERO, o dicionário receberá 
também o ano de contratação e o salário. Calcule e 
acrescente, além da idade, com quantos anos a pessoas vai se 
aposentar.
35 anos de contribuição para se aposentar
''')

from datetime import date

hoje = date.today()

dct = {}
dct['nome'] = input('Digite seu nome: ')
dct['ano_nascimento'] = int(input('Digite seu ano de nascimento: '))
dct['idade'] = hoje.year - dct['ano_nascimento']
dct['ctps'] = int(input('Digite o número da sua CTPS (0 não tem): '))
if dct['ctps'] != 0:
  dct['contratação'] = int(input('Digite o ano de contratação: '))
  dct['salário'] = float(input('Digite o salário: '))
  dct['aponsetadoria'] = dct['contratação'] + 35 - dct['ano_nascimento']

# print(dct)
print('=-' * 20 + '=')
for i, v in dct.items():
  print(f'{i.title()} tem o valor: "{v}"')

