from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 058:
Melhore o jogo do DESAFIO 028 onde o computador vai 
"pensar" em um número entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando 
no final quantos palpites foram necessários para 
vencer.
''')

from random import randint
n1 = randint(0, 10)

c = 1
n2 = int(input('Adivinhe em um número entre 0 e 10: '))
while n1 != n2:
  if n1 > n2:
    msg = 'O número é maior. '
  else:
    msg = 'O número é menor. '
  n2 = int(input('Você errou. {}Tente novamente: '.format(msg)))
  c += 1

print('Acertou! Você precisou de {} tentativas'.format(c))
