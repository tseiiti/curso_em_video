from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 076:
Crie um programa que tenha uma tupla única com nomes de 
produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados 
em forma tabular.
''')

t = (
    'Lápis', 1.75
  , 'Borracha', 2
  , 'Caderno', 15.9
  , 'Estojo', 25
  , 'Transferidor', 4.2
  , 'Compasso', 9.99
  , 'Mochila', 120.32
  , 'Canetas', 22.3
  , 'Livro', 34.9
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(int(len(t) / 2)):
  print(f'{t[i * 2]:.<30}R${t[i * 2 + 1]:8.2f}')
print('-' * 40)
