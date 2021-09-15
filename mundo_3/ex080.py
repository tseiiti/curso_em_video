from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 080:
Crie um programa onde o usuário possa digitar cinco valores 
numéricos e cadastre-os em uma lista, já na posição 
correta de inserção(sem usar o sort.
No final, mostre a lista ordenada na tela.
''')

lst = []
for j in range(5):
  v = int(input('Digite um valor: '))

  i = 0
  while i < len(lst):
    if v < lst[i]:
      break
    i += 1
  lst.insert(i, v)
  print(f'Adicionado na posição {i} da lista')

print('=-' * 20 + '=')
print(f'Você digitou os valores: {lst}')
