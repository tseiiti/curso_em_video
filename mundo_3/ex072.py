from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 072:
Crie um programa que que tenha uma tupla totalmente
preenchida com uma contagem por extenso, de zero até 
vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
e mostrá-lo por extenso.
''')

t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete'
  , 'oito', 'nome', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze'
  , 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  n = int(input('Digite um número entre 0 e 20: '))
  if n in range(0, 21):
    break
  print('Tente novamente. ', end = '')

print(f'Você digitou o número "{t[n]}"')
