from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 101:
Crie um programa que tenha uma função chamada "voto" que 
vai receber como parâmetro o ano de nascimento de uma 
pessoa, retornando um valor literal indicando se uma 
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas 
eleições.
''')

from datetime import date

def voto(ano_nascimento):
  idade = date.today().year - ano_nascimento
  if idade < 16:
    return f'Com {idade}: VOTO NEGADO.'
  elif idade < 18 or idade > 65:
    return f'Com {idade} anos: VOTO OPCINAL.'
  else:
    return f'Com {idade}: VOTO OBRIGATÓRIO.'
  
print(voto(int(input('Em que ano você nasceu? '))))
# print(voto(2003))
# print(voto(2013))
# print(voto(1940))
