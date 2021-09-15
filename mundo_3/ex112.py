from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 112:
Dentro do pacote utilidades_cev que criamos no desafio 111, 
temos um módulo dado. Crie uma função chamada 
leia_dinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que 
sejam monetários.
''')

# from utilidades_cev import moeda
# from utilidades_cev import dado
from utilidades_cev import moeda, dado

p = dado.leia_float('Digite o preço: R$ ')
moeda.resumo(p, 80, 35)
