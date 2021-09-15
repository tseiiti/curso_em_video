from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 052:
Faça um programa que leia um 
número inteiro e diga se ele é 
ou não um número primo.
''')


n = int(input('Digite o primeiro número: '))

r = True
for i in range(2, n):
  if n % i == 0:
    r = False
    break

print(r)
