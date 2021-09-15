from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 056:
Desenvolva um programa que leia o nome, idade e 
sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velhor.
- Quantas mulheres têm menos de 20 anos.
''')

total_idades = 0
idade_velho = 0
quant_mulheres = 0

for i in range(4):
  print('----- {}a pessoa ----'.format(i + 1))
  nome = input('Digite o nome: ')
  idade = int(input('Digite a idade: '))
  sexo = input('Digite o sexo (M ou F): ')

  total_idades += idade

  if sexo.lower() == 'm' and idade_velho < idade:
    idade_velho = idade
    nome_velho = nome

  if sexo.lower() == 'f' and idade < 20:
    quant_mulheres += 1

print('a média de idade é {}'.format(total_idades / 4))
print('o homem mais velho é {}'.format(nome_velho))
print('mulheres novas {}'.format(quant_mulheres))
