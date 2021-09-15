from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 115:
Crie um pequeno sistema modularizado que permita cadastrar 
pessoas pelo seu nome e idade em um arquivo de texto simples. 
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar 
todas as pessoas cadastradas.
''')

from utilidades_cev import dado

arquivo = 'cadastros.txt'

def ler_arquivo():
  try:
    f = open(arquivo, 'r')
    for lin in f:
      l = lin.replace('\n', '').split(';')
      print(f'{l[0]:32}{l[1]:>3} anos')
  except FileNotFoundError as e:
    dado.print_erro('Arquivo não criado. Faça o primeiro cadastro na opção 2.')
    
def insere_arquivo(nome, idade):
  f = open(arquivo, 'a')
  f.write(f'{nome};{idade}\n')
  f.close()
    
while True:
  opcao = dado.menu(
    'Ver pessoas cadastradas', 
    'Cadastrar nova Pessoa', 
    'Sair do Sistema')

  if opcao == 1:
    dado.titulo('1 - pessoas cadastradas')
    ler_arquivo()
  elif opcao == 2:
    dado.titulo('2 - novo cadastro')
    nome = input('Nome: ')
    idade = dado.leia_int('Idade: ')
    insere_arquivo(nome.title(), idade)
  elif opcao == 3:
    print('\n... Saindo do sistema.\n')
    break
  else:
    dado.print_erro('Opção inválida!')
