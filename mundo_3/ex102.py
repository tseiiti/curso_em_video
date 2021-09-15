from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 1002:
Crie um programa que tenha uma função "fatorial" que receba 
dois parâmetros: o primeiro que indique o número a calcular e o 
outro chamado show, que será um valor lógico (opcional) indicando se 
será mostrado ou não na tela o processo de cálculo do fatorial.
''')

def fatorial(num, show = False):
  """Calcula o fatorial de um número.

  Args:
      num (int): O número a ser calculado.
      show (bool, optional): Mostra ou não a conta. Defaults to False.

  Returns: 
      string | int: O valor do Fatorial de um número n.
  """
  res = 1
  msg = ''
  i = 1
  while i < num:
    msg += f'{i} x '
    res *= i
    i += 1
  res *= i
  msg += f'{i} = {res}'
  if show:
    return msg
  else:
    return res

print(fatorial(1))
print(fatorial(2))
print(fatorial(3))
print(fatorial(5))
print(fatorial(1, True))
print(fatorial(2, True))
print(fatorial(3, True))
print(fatorial(5, True))
help(fatorial)