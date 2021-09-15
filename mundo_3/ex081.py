from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 081:
Crie um programa que vai ler vários números e colocar em 
uma lista. 
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor foi digitado e está ou não na lista
''')

lst = []
while True:
  v = int(input('Digite um valor: '))
  lst.append(v)

  r = input('Continua (S/N) ?')
  if r and r in 'Nn':
    break


print('=-' * 20 + '=')
print(f'A) Foram digitados {len(lst)} números')
# lst.sort()
# lst.reverse()
print(f'B) Lista ordenada de forma decrescente {lst.sort(reverse = True)}')
print(f'C) O valor 5 {"" if 5 in lst else "não "}foi digitado')
# if 5 in lst:
#   print('C) O valor 5 foi digitado')
# else:
#   print('C) O valor 5 não foi digitado')
