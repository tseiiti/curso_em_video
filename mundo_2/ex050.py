from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 050:
Desenvolva um programa que leia seis 
números inteiros e mostre a soma 
apenas daqueles que forem pares. Se 
o valor digitado for ímpar, desconsidere-o.
''')

t = 0
c = 0
for i in range(6):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    t += n
    c += 1

print('count = {}, sum = {}'.format(c, t))
