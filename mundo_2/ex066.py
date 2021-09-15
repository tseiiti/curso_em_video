from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 066:
Crie um programa que leia vários números inteiros pelo teclado. O 
programa só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles (desconsiderando o flag).
''')

t = 0
c = 0
n = 0
while True:
  n = int(input('Digite o número a ser somado: '))
  if n == 999:
    break
  c += 1
  t += n

print('você digitou {} números e a soma é {}'.format(c, t))
