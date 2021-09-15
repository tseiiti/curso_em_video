from utilidades_cev import dado

def aumentar(num, per, fmt = False):
  """Aumentar um valor com o percentual indicado

  Args:
      num (numeric): valor a ser aumentado
      per (numeric): percentual do aumento
      fmt (bool, optional): Se será formatado com R$. Defaults to False.

  Returns:
      float | string: resultado aumentado
  """
  res = num + num * (per / 100)
  return moeda(res) if fmt else res
  
def diminuir(num, per, fmt = False):
  """Reduzir um valor com o percentual indicado

  Args:
      num (numeric): valor a ser reduzido
      per (numeric): percentual da redução
      fmt (bool, optional): Se será formatado com R$. Defaults to False.

  Returns:
      float | string: resultado reduzido
  """
  res = num - num * (per / 100)
  return moeda(res) if fmt else res

def dobro(num, fmt = False):
  """Dobra o valor

  Args:
      num (numeric): Valor a ser dobrado
      fmt (bool, optional): Se será formatado com R$. Defaults to False.

  Returns:
      float | string: resultado dobrado
  """
  res = num * 2
  return moeda(res) if fmt else res

def metade(num, fmt = False):
  """Calcula metado do valor

  Args:
      num (numeric): Valor a ser calculado
      fmt (bool, optional): Se será formatado com R$. Defaults to False.

  Returns:
      float | string: resultado calculado
  """
  res = num / 2
  return moeda(res) if fmt else res
  
def moeda(num):
  """Formata um valor em moeda (R$)

  Args:
      num (numeric): valor a ser formatado

  Returns:
      string: valor formatado
  """
  return f'R$ {num:.2f}'.replace('.', ',')

def resumo(num, aum, red):
  """Imprime informações de um preço em formato de resumo

  Args:
      num (numeric): valor a ser analisado
      aum (numeric): porcentagem de aumento
      red (numeric): porcentagem de redução
  """
  tam = 40
  dado.titulo('resumo do valor', tam, '=')
  dado.linha('-', tam)
  print(f'{"Preço analisado":30}{moeda(num):>10}')
  print(f'{"Dobro do preço":30}{dobro(num, True):>10}')
  print(f'{"Metade do preço":30}{metade(num, True):>10}')
  print(f'{aum}{"% de aumento":28}{aumentar(num, aum, True):>10}')
  print(f'{red}{"% de redução":28}{diminuir(num, red, True):>10}')
  dado.linha('-', tam)

