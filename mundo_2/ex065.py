from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 065:
Crie um programa que leia vários números inteiros pelo teclado. No 
final da execução, mostre a média entre todos os valores e qual 
foi o maior e o menor valores lidos. O programa deve perguntar ao 
usuário se ele quer ou não continuar a digitar valores.
''')

tot = con = num = min = max = 0
run = 'S'
while not run or run not in 'nN':
  num = int(input('Digite o número a ser somado: '))
  if con == 0 or num < min:
    min = num
  if con == 0 or num > max:
    max = num
  tot += num
  con += 1
  run = input('Deseja continuar [S/n]? ')

print('a média é {:.2f}, o menor é {}, o maior é {}'.format(tot / con, min, max))
