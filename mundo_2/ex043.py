from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule o IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
''')

n1 = float(input('Digite sua altura: '))
n2 = float(input('Digite seu peso: '))

# converte centimetro em metros
if n1 > 100:
  n1 = n1 / 100
imc = n2 / n1 ** 2

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
  print('Abaixo do Peso')
elif imc <= 25:
  print('Peso ideal')
elif imc <= 30:
  print('Sobrepeso')
elif imc <= 40:
  print('Obesidade')
else:
  print('Obesidade mórbida')
