def aumentar(num, per, fmt = False):
  if fmt:
    return moeda(num + num * (per / 100))
  else:
    return num + num * (per / 100)

def diminuir(num, per, fmt = False):
  if fmt:
    return moeda(num - num * (per / 100))
  else:
    return num - num * (per / 100)

def dobro(num, fmt = False):
  if fmt:
    return moeda(num * 2)
  else:
    return num * 2

def metade(num, fmt = False):
  if fmt:
    return moeda(num / 2)
  else:
    return num / 2

def moeda(num):
  return f'R$ {num:.2f}'

def linha(char, tam):
  print(char * tam)

def titulo(texto, tam, char):
  linha(char, tam)
  texto = texto.strip().upper()
  space = ' ' * int((tam - len(texto) - 4) / 2)
  texto = char + char + space + texto + space
  if len(texto) < tam - 2:
    texto += ' '
  texto += char + char
  print(f'{texto}')
  linha(char, tam)

def resumo(num, aum, red):
  tam = 40
  titulo('resumo do valor', tam, '=')
  linha('-', tam)
  print(f'{"Preço analisado":30}{moeda(num):>10}')
  print(f'{"Dobro do preço":30}{dobro(num, True):>10}')
  print(f'{"Metade do preço":30}{metade(num, True):>10}')
  print(f'{aum}{"% de aumento":28}{aumentar(num, aum, True):>10}')
  print(f'{red}{"% de redução":28}{diminuir(num, red, True):>10}')
  linha('-', tam)

