from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 104:
Crie um programa que tenha a função "leia_int", que vai
funcionar de forma semelhante à função input do Python, só 
que fazendo a validaçào para aceitar apenas um valor numérico.
Ex:
n = leia_int('Digite um n')
''')

def leia_int(msg = ''):
  while True:
    valor = input(msg).strip()
    if valor.isnumeric():
      return int(valor)
    else:
      print('\033[1;31mErro, Digite um número inteiro válido.\033[m')

  

n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
