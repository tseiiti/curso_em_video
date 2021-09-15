from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 085:
Crie um programa onde o usuário possa digitar sete valores 
numéricos e cadastre-os em uma lista única que 
mantenha separados os valores pares e ímpares. No final, 
mostre os valores pares e ímpares em ordem crescente.
''')

lst = [[], []]
for i in range(7):
  n = int(input(f'Digite o {i + 1}° valor: '))
  lst[n % 2].append(n)

lst[0].sort()
lst[1].sort()

print('=-' * 20 + '=')
# print(f'Os valores pares digitados foram: {sorted(lst[0])}')
# print(f'Os valores ímpares digitados foram: {sorted(lst[1])}')
print(f'Os valores pares digitados foram: {lst[0]}')
print(f'Os valores ímpares digitados foram: {lst[1]}')
