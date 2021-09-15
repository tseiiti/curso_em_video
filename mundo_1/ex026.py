from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 026:
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
''')

n = input('Digite uma frase: ').strip()
print('quantas letras "A": {}'.format(n.lower().count('a')))
print('posição da primeira letra "A": {}'.format(n.lower().find('a') + 1))
print('posição da última letra "A": {}'.format(n.lower().rfind('a') + 1))
