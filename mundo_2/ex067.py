from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 067:
Faça um programa que mostre a tabuada de vários números inteiros, um 
de cada vez, para cada valor digitado pelo usuário. O programa 
será interrompido quando o número solicitado for negativo.
''')

while True:
  n = int(input('Digite um número: '))
  if n < 0:
    break
  for i in range(1, 11):
    print(f'{n} X {i:2} = {n * i:2}')
