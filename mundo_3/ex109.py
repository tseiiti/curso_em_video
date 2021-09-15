from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 109:
Modifique as funções que foram criadas no desafio 107 
para que elas aceitem um parâmetro a mais informando se o valor 
retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108.
''')

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% em {moeda.moeda(p)} é {moeda.aumentar(p, 10, True)}')
print(f'Reduzir 13% em {moeda.moeda(p)} é {moeda.diminuir(p, 13, True)}')

