from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 062:
Refaça o DESAFIO 061, perguntando para o usuário se ele quer mostrar 
mais alguns termos. O programa encerra quando ele disser que quer 
mostrar 0 termos.
''')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite a razão: '))

n = 10
i = -1
while n != 0:
  # soma para próxima PA não repetir
  i += 1
  n += i

  while i < n - 1:
    print(n1 + i * n2, end=' -> ')
    i += 1
  print(n1 + i * n2) # imprime último número sem flechinha

  n = int(input('deseja mostrar mais quantos termos? '))

print('Progressão finalizada com {} termos'.format(i + 1))
