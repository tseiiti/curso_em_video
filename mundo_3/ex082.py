from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 082:
Crie um programa que vai ler vários números e colocar em 
uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os 
valores pares e os ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
''')

l1 = []
l2 = []
l3 = []
while True:
  v = int(input('Digite um valor: '))
  l1.append(v)

  r = input('Continua (S/N) ?')
  if r and r in 'Nn':
    break

for i in l1:
  if i % 2 == 0:
    l2.append(i)
  else:
    l3.append(i)

print('=-' * 20 + '=')
print(f'Lista total: {l1}')
print(f'Lista pares: {l2}')
print(f'Lista ímpares: {l3}')
