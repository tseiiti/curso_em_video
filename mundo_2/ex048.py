from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 048:
Faça um programa que calcule a soma 
entre todos os números ímpares que são 
múltiplos de três e que se encontram no 
intervalo de 1 até 500.
''')

t = 0
c = 0
for i in range(3, 501, 3):
  if i % 2 != 0:
    t += i
    c += 1
    # print('{} '.format(i), end='')

print('count = {}, sum = {}'.format(c, t))

# t = 0
# for i in range(1, 501):
#   if i % 2 != 0 and i % 3 == 0:
#     t += i
#     # print(i)

# print(t)
