def leia_float(msg = 'Digite um valor'):
  """Permite o input de um float sem a possibilidade de erro

  Args:
      msg (str, optional): Mensagem do input. Defaults to 'Digite um valor'.

  Returns:
      float: Valor float
  """
  while True:
    valor = input(msg + '\033[3;32;40m').replace(',', '.')
    print('\033[m', end='')
    try:
      return float(valor)
    except ValueError:
      print_erro('Erro, valor inválido!')

  # txts = ('123', 'abc', '', '0', '0.123', '-456', '-0456', '0.456', '12.456')
  # for txt in txts:
  #   print(f'"{txt}" isnumeric: {txt.isnumeric()}')
  #   print(f'"{txt}" isdecimal: {txt.isdecimal()}')
  #   print(f'"{txt}" isalpha: {txt.isalpha()}')
  #   print(f'"{txt}" isalnum: {txt.isalnum()}')
  #   print(f'"{txt}" isdigit: {txt.isdigit()}')

def leia_int(msg = 'Digite um valor'):
  """Permite o input de um int sem a possibilidade de erro

  Args:
      msg (str, optional): Mensagem do input. Defaults to 'Digite um valor'.

  Returns:
      int: Valor int
  """
  while True:
    valor = input(msg + '\033[3;32m')
    print('\033[m', end='')
    try:
      return int(valor)
    except ValueError:
      print_erro('Erro, valor inválido!')

def print_erro(msg = 'Erro'):
  """Imprime mensagem de erro em cor vermelha negrito

  Args:
      msg (str, optional): Mensagem de erro. Defaults to 'Erro'.
  """
  print(f'\033[1;31m{msg}\033[m')
    
def linha(tam = 40, char = '-'):
  """Imprime linha de acordo com o tamanho e caractere escolhido

  Args:
      char (str, optional): caractere de impressão. Defaults to '-'.
      tam (int, optional): tamanho da linha. Defaults to 80.
  """
  print(char * tam)

def titulo(texto = '', tam = 40, char = '-'):
  """Imprime um título de acordo com o texto escolhido desenhando uma linha antes de depois

  Args:
      texto (str, optional): texto do título. Defaults to ''.
      tam (int, optional): tamanho da linha. Defaults to 80.
      char (str, optional): caractere de impressão da linha. Defaults to '='.
  """
  print()
  linha(tam, char)
  texto = texto.strip().upper()
  space = ' ' * int((tam - len(texto) - 4) / 2)
  texto = char + char + space + texto + space
  if len(texto) < tam - 2:
    texto += ' '
  texto += char + char
  print(f'{texto}')
  linha(tam, char)

def menu(* itens):
  """Desenha um menu

  Returns:
      tupla(opções): Tupla de opções
  """
  titulo('menu principal')
  for i, v in enumerate(itens, 1):
    print(f'\033[32m[{i:^3}] \033[36m{v}\033[m')
  linha(40, '-')
  while True:
    opc = leia_int('Escolha uma opção: ')
    if 1 <= opc <= len(itens):
      return opc
    print_erro('Erro, opção inválida!')
