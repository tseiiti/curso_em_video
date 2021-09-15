from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 047:
Crie um programa que mostre na 
tela todos os números pares que 
estão no intervalo entre 1 e 50.
''')

for i in range(2, 51, 2):
  print('{} '.format(i), end='')
  
# for i in range(1, 51):
#   if i % 2 == 0:
#     print('{} '.format(i), end='')
