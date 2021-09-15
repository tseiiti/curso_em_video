from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 079:
Crie um programa onde o usuário possa digitar vários valores 
numéricos e cadastre-os em uma lista. Caso o número já 
exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente.
''')

lst = []
while True:
  n = input('Digite um valor: ')
  if n in lst:
    print('Valor duplicado')
  else:
    lst.append(n)

  r = input('Continua (S/N) ?')
  if r and r in 'Nn':
    break

print(f'Você digitou os valores {sorted(lst)}')
