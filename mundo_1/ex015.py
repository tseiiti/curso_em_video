from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 015:
Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.
''')

n1 = float(input('Quantidade de dias alugado: '))
n2 = float(input('Quantidade de kilometros percorridos: '))
print('Total a pagar R$ {:.2f}'.format(n1 * 60 + n2 * 0.15))
