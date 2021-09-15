from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 078:
Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as 
suas respectivas posições na lista
''')

lst = []
for i in range(5):
  lst.append(input(f'Digite o {i + 1}° valor: '))

print('=' * 40)
print(f'A lista é: {lst}')

m = max(lst)
print(f'o maior valor foi {m} nas posições: ', end= '')
for i, v in enumerate(lst):
  if v == m:
    print(i, end= '... ')
print()
# i = 0
# while True:
#   j = lst.index(m, i)
#   i = j + 1
#   print(i, end= '')
#   if m in lst[i:]:
#     print(', ', end='')
#   else:
#     print(')')
#     break
    

m = min(lst)
print(f'o menor valor foi {m} nas posições: ', end= '')
for i, v in enumerate(lst):
  if v == m:
    print(i, end= '... ')
print()
# i = 0
# while True:
#   j = lst.index(m, i)
#   i = j + 1
#   print(i, end= '')
#   if m in lst[i:]:
#     print(', ', end='')
#   else:
#     print(')')
#     break
