from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 100:
Faça um programa que tenha uma lista chamada "numeros" e 
duas funções chamadas sorteia() e soma_par(). A primeira 
função vai sortear 5 números e colocá-los dentro da lista e a 
segunda função vai mostrar a soma entre todos os valores 
PARES sorteados pela função anterior.
''')

from random import randint

def sorteia(numeros):
  print('Sorteando 5 valores da lista: ', end='')
  for i in range(5):
    n = randint(0, 9)
    print(f'{n} ', end='')
    numeros.append(n)
  print('PRONTO!')

def soma_par(numeros):
  t = 0
  for i in numeros:
    if i % 2 == 0:
      t += i
  print(f'Somando os valores pares de {numeros}, temos {t}')

numeros = []
sorteia(numeros)
soma_par(numeros)
