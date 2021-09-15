from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 103:
Faça um programa que tenha uma função chamada "ficha", que 
receba dois parâmetros opcionais: o nome de um 
jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo 
que algum dado não tenha sido informado corretamente.
''')

def ficha(nome = '<desconhecido>', gols = 0):
  if not gols.isnumeric():
    gols = 0
  return f'O jogador {nome} fez {gols} gols(s) no campeonato.'


print(ficha(
  input('Nome do Jogador: '), 
  input('Número de Gols: ')
  ))

