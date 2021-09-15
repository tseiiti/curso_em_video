from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 010:
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos Dólares ela pode comprar.
Considere US$1,00 = R$3,27
''')

n = float(input('Valor na carteira: R$'))
print('valor em dólar é: U${:.2f}'.format(n / 3.27))
