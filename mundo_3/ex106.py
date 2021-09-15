from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 106:
Faça um mini-sistema que utilize o Interactve Help do 
Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará.
Obs: use cores.
''')

    

cor = (
  '\033[m' # reset: 0
  , '\033[0;37;40m' # normal: 1
  , '\033[3;32;40m' # verde: 2
  , '\033[0;30;47m' # enfase: 3
  , '\033[1;36;47m' # subtitulo: 4
  , '\033[1;37;46m' # titulo: 5
  , '\033[3;37;40m' # italico: 6
  , '\033[7;30m' # branco: 7
)

def meu_print(texto, cor):
  print(f'{cor}{texto}\033[m')

def titulo(texto, char, cor):
    meu_print(char * 80, cor)
    meu_print(f'{texto:^80}', cor)
    meu_print(char * 80, cor)

def ajuda():
  while True:
    titulo('SISTEMA DE AJUDA', '*', cor[5])

    obj = input(f'{cor[6]}Função ou Biblioteca > {cor[2]}')
    print(cor[1])
    if obj.upper() == 'FIM':
      break

    titulo(f'Acessando o manual do comando "{obj}"', '-', cor[4])

    texto = help(obj)
    meu_print(texto, cor[7])

ajuda()
