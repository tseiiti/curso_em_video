from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 083:
Crie um programa onde o usuário digite uma expressão 
qualquer que use parênteses. Seu aplicativo deverá 
analisar se a expressão passada está com os parênteses 
abertos e fechados na ordem correta.
''')

e = input('Digite uma expressão: ')
# e = '((a+b)*c'

a = 0
b = True
for c in e:
  if c == ')' and a <= 0:
    b = False
    break
  if c == '(':
    a += 1
  if c == ')':
    a -= 1

print('=-' * 20 + '=')
if a == 0 and b:
  print('Sua expressão está válida!')
else:
  print('Sua expressão está inválida!')
