from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 046:
Faça um programa que mostre na tela uma 
contagem regressiva para o estouro de 
fogos de artifício, indo de 10 até 0, com 
uma pausa de 1 segundo entre eles.
''')

print('''DESAFIO 045:
Crie um programa que 
''')

from time import sleep

for i in range(10, -1, -1):
  print(i)
  sleep(1)

print('Fogo!')
