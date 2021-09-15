from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 074:
Crie um programa que vai gerar cinco números aleatórios e 
colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também 
indique o menor e o maior valor que estão na tupla.
''')

from random import randint

# n1 = randint(1, 10)
# n2 = randint(1, 10)
# n3 = randint(1, 10)
# n4 = randint(1, 10)
# n5 = randint(1, 10)
# t = (n1, n2, n3, n4, n5)
t = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Lista: {" ".join(str(c) for c in t)}')
print(f'menor: {min(t)}')
print(f'maior: {max(t)}')
