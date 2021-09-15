from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 063:
Escreva um programa que leia um número n inteiro qualquer e
mostre na tela os n primeiros elementos de uma Sequência de 
Fibonacci.
''')

n = int(input('Digite um número: '))

i = 1
p = -1  #penúltimo termo
u = 1   #último termo
while i < n:
  f = u + p
  p = u
  u = f
  i += 1
  print(f, end=' -> ')
print(u + p)
