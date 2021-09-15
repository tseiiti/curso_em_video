from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 097:
Faça um programa que tenha uma função chamada escreva(), que 
receba um texto qualquer como parâmetro e mostre 
uma mensagem com tamanho adaptável.
Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
''')

def escreva(texto):
  print('~' * (len(texto) + 4))
  print(f'  {texto}  ')
  print('~' * (len(texto) + 4))


escreva('Gustavo Guanabara')
escreva('Curson de Python no YouTube')
escreva('CeV')
