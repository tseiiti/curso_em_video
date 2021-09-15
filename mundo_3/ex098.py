from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 098:
Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim, e passo e realize a 
contagem.
Seu programa tem que realizar três contagens através da 
função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, 2 em 2
c) Um contagem personalizada.
''')

from time import sleep

def contagem(inicio, fim, passo):
  if passo == 0:
    passo = 1
    
  if inicio > fim and passo > 0:
    passo *= -1

  fim += 1 if inicio < fim else -1    

  for i in range(inicio, fim, passo):
    print(f'{i}, ', end='')
    sleep(0.5)
  print('acabou!')

contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
