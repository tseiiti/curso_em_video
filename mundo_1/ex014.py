from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 014:
Escreva um programa que converta uma temperatura
digitada em °C e converta para °F.
''')

n = float(input('Digite a temperatura em C° (Celcius): '))
print('em Fahrenheit {:.2f}'.format(n * 9 / 5 + 32))
