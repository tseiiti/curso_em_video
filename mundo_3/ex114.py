from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 114:
Crie um código em Python que teste se o site Pudim está 
acessível pelo computador usado.
''')

import requests

try:
  req = requests.get('http://pudim.com.br/')
  print('Consegui acessar o site Pudim com sucesso!')
except:
  print('O site Pudim não está acessível no momento.')
