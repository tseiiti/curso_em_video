from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 095:
Aprimore o DESAFIO 093 para que ele funcione com vários 
jogadores, incluindo um sistema de visualizaçào de 
detalhes do aproveitamento de cada jogador.
''')

lst = []
dct = {}
while True:
  dct['nome'] = input('Nome do jogador: ')
  dct['partidas'] = int(input('Total de partidas: '))
  dct['gols'] = []
  dct['total'] = 0
  for i in range(dct['partidas']):
    n = int(input(f'Quantos gols na partida {i + 1}: '))
    dct['gols'].append(n)
    dct['total'] += n
  lst.append(dct.copy())

  r = input('Continua (S/N) ?')
  if r and r in 'Nn':
    break
  print('-' * 40)

print('=-' * 20 + '=')
print(f"{'cod':<4}{'nome':15}{'gols':15}{'total':6}")
print('-' * 40)
for dct in lst:
  print(f"{lst.index(dct):<4}{dct['nome']:15}{str(dct['gols']):15}{dct['total']:6}")

n = 0
while n != 999:
  n = int(input('Mostrar dados de qual jogador (999 parar): '))
  if n in range(len(lst)):
    print(f"O jogador {lst[n]['nome']} jogou {lst[n]['partidas']} partidas.")
    for i, v in enumerate(lst[n]['gols']):
      print(f"  - Na partida {i}, fez {v} gols.")
  else:
    print('Tente outro código. ', end='')