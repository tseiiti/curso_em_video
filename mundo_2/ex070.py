from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 070:
Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai continuar. 
No final, mostre:
- A) Qual é o total gasto na compra.
- B) Quantos prdutos custam mais de R$1000.
- C) Qual nome do produto mais barato.
''')

contador = 0
total_gasto = 0
mais_de_1000 = 0
mais_barato_preco = 0
mais_barato_nome = ''

while True:
  nome = input('Nome do produto: ')
  preco = float(input('Preço do produto: R$ '))

  if preco > 1000:
    mais_de_1000 += 1

  if preco < mais_barato_preco or contador == 0:
    mais_barato_preco = preco
    mais_barato_nome = nome
  
  total_gasto += preco
  contador += 1

  c = ''
  while not c or c not in 'SN':
    c = input('Deseja continuar S/N: ').strip()[0].upper()
  if c == 'N':
    break

print(f'A) Total de gasto na compra: {total_gasto}')
print(f'B) Quantidade de produtos mais de R$1000: {mais_de_1000}')
print(f'C) Produto mais barato: {mais_barato_nome}')
