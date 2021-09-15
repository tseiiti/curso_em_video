from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 110:
Adicione ao módulo moeda.py criado nos desafios anteriores, 
uma função chamada resumo(), que mostre na tela algumas 
informações geradas pelas funções que já temos no módulo cirado 
até aqui.
''')

import moeda

# p = float(input('Digite o preço: R$ '))
p = 500
moeda.resumo(p, 80, 35)
