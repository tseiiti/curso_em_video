from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 055:
Faça um programa que leia o peso de 
cinco pessoas. No final, mostre qual 
foi o maior e o menor peso lidos.
''')

t = []
for i in range(5):
  t.append(float(input('Digite o peso: ')))
t.sort()

print('o menor peso foi {}'.format(t[0]))
print('o maior peso foi {}'.format(t[4]))
