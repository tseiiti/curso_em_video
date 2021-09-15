from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 053:
Crie um programa que leia uma frase qualquer e diga 
se ela é um palíndromo, desconsiderando os espaços.
Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
''')

f = input('Digite a frase: ')
f = f.replace(' ', '').upper()

s = ''
for i in range(len(f) - 1, -1, -1):
  s += f[i]

# print(f)
# print(s)

if f == s:
  print('é palíndromo')
else:
  print('não é palíndromo')
