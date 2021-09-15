from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 073:
Crie um uma tupla preenchida com os 20 primeiros colocados 
da Tabela do Campeonato Brasileiro de Futebol, na ordem 
de colocação. Depois mostre:
A) Apenas os 5 primeros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
''')

t = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense'
  , 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife'
  , 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')


print(f'A Lista de times do Brasileirão: {t}')
print(f'A) Os 5 primeiros são: {t[:5]}')
print(f'B) Os 4 últimos são: {t[-4:]}')
print(f'C) Times em ordem alfabética: {tuple(sorted(t))}')
print(f'D) Chapeoense está na {t.index("Chapecoense") + 1}ª posição')
