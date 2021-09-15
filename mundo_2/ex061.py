from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 061:
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando 
os 10 primeiros termos da progressão usando a estrutura while.
''')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite a razão: '))

# i = 1
# pa = n1
# while i < 9:
#   print(pa, end=' -> ')
#   pa += n2
#   i += 1
# print(pa + n2)

i = 0
while i < 9:
  print(n1 + i * n2, end=' -> ')
  i += 1
print(n1 + 9 * n2)
