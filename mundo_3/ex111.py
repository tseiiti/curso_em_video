from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 111:
Crie um pacote chamado utilidades_cev que tenha dois módulos 
internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 
para o primeiro pacote e mantenha tudo funcionando.
''')

from utilidades_cev import moeda

# p = float(input('Digite o preço: R$ '))
p = 500
moeda.resumo(p, 80, 35)
