from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 090:
Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, 
mostre o conteúdo da estrutura na tela.
''')

dct = {
  'nome': input('Digite o nome: ')
}
dct['média'] = float(input(f'Digite a média de {dct["nome"]}: '))
if dct['média'] >= 7:
  dct['situação'] = 'aprovado'
elif dct['média'] >= 5:
  dct['situação'] = 'recuperação'
else:
  dct['situação'] = 'reprovado'

# print(dct)
print('=-' * 20 + '=')
for i, v in dct.items():
  print(f'{i.title()} tem o valor: "{v}"')
