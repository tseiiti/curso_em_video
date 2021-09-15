from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 113:
Reescreva a função leia_int() que fizemos no desafio 104, incluindo 
agora a possibilidade da digitaçào de um número de tipo inválido. 
Aproveite e crie também a função leia_float() com a mesma funcionalidade.
''')

from utilidades_cev import dado

a = dado.leia_int('Digite um Inteiro: ')
b = dado.leia_float('Digite um Real: ')
print(f'O valor inteiro digitado foi {a} e o real foi {b}')
