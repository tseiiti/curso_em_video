from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 051:
Desenvolva um programa que leia o 
primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros 
termos dessa progressão.
''')


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite a razão: '))

for i in range(9):
  print(n1 + i * n2, end=' -> ')
print(n1 + 9 * n2)
