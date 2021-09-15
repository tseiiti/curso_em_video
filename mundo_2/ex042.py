from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 042:
Refaça o DESAFIO 035  dos triângulos, acrescetando o recurso de
mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
''')

n = []
n.append(float(input('Informe a reta 1: ')))
n.append(float(input('Informe a reta 2: ')))
n.append(float(input('Informe a reta 3: ')))
n.sort()

if n[0] + n[1] > n[2]:
  if n[0] == n[1] == n[2]:
    print('Equilátero')
  elif n[0] == n[1] or n[0] == n[2] or n[1] == n[2]:
    print('Isósceles')
  else:
    print('Escaleno')
else:
  print('não forma um triângulo')
