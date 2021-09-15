from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 105:
Faça um programa que tenha a função "notas" que pode 
receber várias notas de alunos e vai retornar um dicionário 
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.
''')

def notas(* nts, sit = False):
  """Função para analisar notas e situações de vários alunos.

  Args:
      nts (tupla): várias notas
      sit (bool, optional): Indica se deve ou não adicionar a situação. Defaults to False.

  Returns:
      dict: Várias informações sobre a situação da turma.
  """
  rsp = {
    'total': len(nts), 
    'maior': max(nts), 
    'menor': min(nts), 
    'média': sum(nts) / len(nts)
  }

  # rsp = {
  #   'total': 0, 
  #   'maior': 0.0, 
  #   'menor': 0.0, 
  #   'média': 0.0
  # }

  # som = 0
  # for n in nts:
  #   n = float(n)
  #   som += n
  #   if rsp['total'] == 0 or rsp['maior'] < n:
  #     rsp['maior'] = n
  #   if rsp['total'] == 0 or rsp['menor'] > n:
  #     rsp['menor'] = n
  #   rsp['total'] += 1
  # rsp['média'] = som / rsp['total']

  if sit:
    if rsp['média'] < 5:
      rsp['situação'] = 'RUIM'
    elif rsp['média'] < 7:
      rsp['situação'] = 'RAZOÁVEL'
    else:
      rsp['situação'] = 'BOA'
        
  return rsp

print(notas(5.5, 9.5, 10, 6.5))
print(notas(5.5, 9.5, 10, 6.5, sit = True))
print(notas(4.5, 10, 6.5, sit = True))
print(notas(3.5, 10, 6.5, sit = True))
print(notas(3.5, 2, 6.5, sit = True))
print(notas(3.5, 2, 6.5, 2, 7, 4, sit = True))
help(notas)
