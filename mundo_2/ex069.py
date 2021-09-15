from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 069:
Crie um programa que leia a idade e o sexo de várias 
pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
- A) Quantas pessoas tem mais de 18 anos.
- B) Quantos homens foram cadastrados.
- C) Quantas mulheres têm menos de 20 anos.
''')

adultos = 0
homens = 0
moças = 0

while True:
  idade = int(input('Digite a idade: '))
    
  sexo = ''
  while not sexo or sexo not in 'MF':
    sexo = input('Digite o sexo (M ou F): ').strip()[0].upper()

  if idade > 18:
    adultos += 1

  if sexo == 'M':
    homens += 1

  if sexo == 'F' and idade < 20:
    moças += 1

  c = ''
  while not c or c not in 'SN':
    c = input('Deseja continuar S/N: ').strip()[0].upper()
  if c == 'N':
    break

print(f'A) Pessoas com mais de 18 anos: {adultos}')
print(f'B) Quantidade de homens: {homens}')
print(f'C) Mulheres com menos de 20 anos: {moças}')
