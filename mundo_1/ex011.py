from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 011:
Faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
''')

n1 = float(input('Digite a largura da parede: '))
n2 = float(input('Digite a altura da parede: '))
print('a área é: {:.2f}'.format(n1 * n2))
print('precisa de {:.2f} litros de tinta'.format(n1 * n2 / 2))
