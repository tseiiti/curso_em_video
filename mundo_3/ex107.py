from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 107:
Crie um módulo chamado moeda.py que tenha as funções 
incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use 
algumas dessas funções.
''')

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% em {p} é {moeda.aumentar(p, 10)}')
print(f'Reduzir 13% em {p} é {moeda.diminuir(p, 13)}')

