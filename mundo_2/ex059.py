from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 059:
Crie um programa que leia dois valores e mostre um menu como o 
a baixo na tela:
Seu programa deverá realizar a operação solicitada em cada caso.
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')

n1 = 0
n2 = 0
o = '4'
while o != '5':

  if o and o in '123':
    print('=' * 40)
    if o == '1':
      print('[ 1 ] SOMAR: {} + {} = {}'.format(n1, n2, n1 + n2))

    if o == '2':
      print('[ 2 ] MULTIPLICAR: {} x {} = {}'.format(n1, n2, n1 * n2))

    if o == '3':
      print('[ 3 ] MAIOR: entre {} e {} = {}'.format(n1, n2, max([n1, n2])))

    print('=' * 40)
    print('')

  if o == '4':
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    system('cls' if name == 'nt' else 'clear')

  print('=> 1° número: {} | 2° número: {}'.format(n1, n2))
  print('''
Escolha uma função:
  [ 1 ] SOMAR
  [ 2 ] MULTIPLICAR
  [ 3 ] MAIOR
  [ 4 ] NOVOS NÚMEROS
  [ 5 ] SAIR''')
  # print('[ 1 ] SOMAR')
  # print('[ 2 ] MULTIPLICAR')
  # print('[ 3 ] MAIOR')
  # print('[ 4 ] NOVOS NÚMEROS')
  # print('[ 5 ] SAIR')
  o = input('Escolha uma opção: ')

  system('cls' if name == 'nt' else 'clear')