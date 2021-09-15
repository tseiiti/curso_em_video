from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 057:
Faça um programa que leia o sexo de uma 
pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação 
novamente até ter um valor correto.
''')

r = ''
while not r or r not in 'MFmf':
# while not r or 'MFmf'.find(r) == -1:
  r = input('Sexo [M/F]: ').strip()[0]
  
print(r)
