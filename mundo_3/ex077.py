from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 077:
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para 
cada palavra, quais são as suas vogais.
''')

t = ('aprender'
  , 'programar'
  , 'linguagem'
  , 'python'
  , 'curso'
  , 'gratis'
  , 'estudar'
  , 'praticar'
  , 'trabalhar'
  , 'mercado'
  , 'programador'
  , 'futuro'
)

for p in t:
  print(f'\nNa palavra {p.upper()} temos ', end='')
  for c in p:
    if c.lower() in 'aeiou':
      print(c, end=' ')
