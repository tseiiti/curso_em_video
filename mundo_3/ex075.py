from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 075:
Desenvolva um programa que leia quatro valores pelo 
teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
''')

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# n3 = int(input('Digite mais um número: '))
# n4 = int(input('Digite o último número: '))
# t = (n1, n2, n3, n4)

t = (
  int(input('Digite um número: '))
  , int(input('Digite outro número: '))
  , int(input('Digite mais um número: '))
  , int(input('Digite o último número: '))
)

print(f'Lista: {t}')
print(f'O valor 9 apareceu: {t.count(9)} vezes')

if 3 in t:
  print(f'O valor 3 apareceu na: {t.index(3) + 1}ª posição')
else:
  print(f'O valor 3 não foi digitado nenhuma vez')

print(f'Os valores pares digitados foram ', end='')
for i in t:
  if i % 2 == 0:
    print(f'{i} ', end='')
print('')
