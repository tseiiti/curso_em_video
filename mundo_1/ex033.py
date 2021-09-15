from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 033:
Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.
''')

n = []
n.append(int(input('Número 1: ')))
n.append(int(input('Número 2: ')))
n.append(int(input('Número 3: ')))
n.sort()

print('o maior número é {}'.format(n[2]))
print('o menor número é {}'.format(n[0]))

# n1 = int(input('Número 1: '))
# n2 = int(input('Número 2: '))
# n3 = int(input('Número 3: '))

# if n1 > n2 and n1 > n3:
#   print('o maior número é {}'.format(n1))
# if n2 > n1 and n2 > n3:
#   print('o maior número é {}'.format(n2))
# if n3 > n1 and n3 > n2:
#   print('o maior número é {}'.format(n3))

# if n1 < n2 and n1 < n3:
#   print('o menor número é {}'.format(n1))
# if n2 < n1 and n2 < n3:
#   print('o menor número é {}'.format(n2))
# if n3 < n1 and n3 < n2:
#   print('o menor número é {}'.format(n3))
