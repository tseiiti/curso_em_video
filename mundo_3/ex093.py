from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 093:
Crie um programa que gerencie o aproveitamento de um 
jogador de futebol. O programa vai ler o nome do jogador e 
quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em 
um dicionário,incluindo o total de gols feitos durante o 
campeonato.
''')

dct = {}
dct['nome'] = input('Nome do jogador: ')
dct['partidas'] = int(input('Total de partidas: '))
dct['gols'] = []
dct['total'] = 0
for i in range(dct['partidas']):
  n = int(input(f'Quantos gols na partida {i + 1}: '))
  dct['total'] += n
  dct['gols'].append(n)

print('=-' * 20 + '=')
print(dct)

print('=-' * 20 + '=')
for i, v in dct.items():
  print(f'{i.title()} tem o valor: "{v}"')


print('=-' * 20 + '=')
print(f"O jogador {dct['nome']} jogou {dct['partidas']}.")
for i, v in enumerate(dct['gols']):
  print(f"  - Na partida {i + 1}, fez {v} gols.")
print(f"O jogador fez um total de {dct['total']} gols.")
