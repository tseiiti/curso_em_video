from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 099:
Faça um programa que tenha uma função chamada maior(), que 
receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual 
deles é o maior
''')

def maior(*tpl):
  print('Analisando os valores passados...')
  m = 0
  for i, v in enumerate(tpl):
    print(f'{v} ', end= '')
    if m < v or i == 0:
      m = v
  print(f'Foram informados {len(tpl)} valores')
  print(f'O maior valor foi {m}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
