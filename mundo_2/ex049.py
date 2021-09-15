from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 049:
Refaça o DESAFIO 009, motrando a 
tabuada de um número que o usuário 
escolher, só que agora utilizando um laço for.
''')

n = int(input('Digite um número: '))
for i in range(1, 11):
  print('{} X {:2} = {:2}'.format(n, i, n * i))
