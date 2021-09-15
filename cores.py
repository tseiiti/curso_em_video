from os import system, name
system('cls' if name == 'nt' else 'clear')

print(f'\n\n\033[7;37mTeste!\033[m\n\n')
print('curso em video'[:5])


for b in range(0, 8):
  for t in range(0, 8):
    for s in [0, 1, 3, 4, 7]:
      if b != t or s == 1:
        if s == 7:
          print(f'\033[{s};3{b};4{t}mOlá, Mundo! => Estilo: {s} | Texto: 3{b} | Fundo: 4{t}\033[m')
        else:
          print(f'\033[{s};3{t};4{b}mOlá, Mundo! => Estilo: {s} | Texto: 3{t} | Fundo: 4{b}\033[m')


# for b in range(0, 10):
#   for t in range(0, 10):
#     for s in range(0, 10):
#       print(f'\033[{s};3{b};4{t}mOlá, Mundo! => Estilo: {s} | Texto: 3{b} | Fundo: 4{t}\033[m')
