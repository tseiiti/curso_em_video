from os import system, name
system('cls' if name == 'nt' else 'clear')


# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr[1])
# print([1, 2, 3, 4].index(3))
# print(type(arr))
# l = list(arr)
# print(l.index(3))

# def teste(x):
#   if x == 1:
#     return 'asdfa'
#   elif x == 2:
#     return None
#   else:
#     return

# print(teste(1))
# print(teste(2))
# print(teste(3))

# s = '1000 2 3 800'
# l = [int(i) for i in s.split(' ')]
# a = l[0]
# m = l[1]
# n = l[2]
# x = l[3] - l[0]
    
# print(int((a * m) + (x * n)))


# import math
# print(math.ceil(5.67))
# print(math.floor(5.67))


# s = '5.090 5.09'
# l = s.split(' ')
# print('Y' if l[0] < l[1] else 'N')

# l = [float(i) for i in s.split(' ')]
# print('Yes' if l[0] < l[1] else 'No')
# print(l)



# from datetime import datetime
# f = open('teste_python.txt', 'w')
# n = 999999
# ini = datetime.now()
# s = str(n ** n)
# fim = datetime.now()

# f.write(f'inicio: {ini}\n')
# f.write(f'termin: {fim}\n')
# f.write(f'{s}\n')
# f.close()

# x = ('ve', 'cad', 'sai')
# print(len(x))
# print(len(str(len(x))))

# num = [2, 8, 4, 7]
# print(num)
# num.pop()
# print(num)
# num.insert(1, 3)
# print(num)
# num.append(6)
# print(num)

# import math
# for i in range(1, 11):
#   for j in range(10):
#     print(f'{i + j * 10:.<3}: {math.log(i + j * 10):18}', end=', ')
#   print()

# print('-' * 80)
# for i in range(1, 11):
#   for j in range(10):
#     print(f'{i + j * 10:.<3}: {math.log(i + j * 10, 10):18}', end=', ')
#   print()

# print('-' * 80)
# for i in range(1, 11):
#   for j in range(10):
#     print(f'{i + j * 10:.<3}: {math.floor(math.log(i + j * 10, 10)):18}', end=', ')
#   print()



# try:
#   a = int(input('a: '))
#   b = int(input('b: '))
#   x = a / b
# except ValueError as ex:
#   print(f'ValueError: {ex} | {ex.__class__}')
# except ZeroDivisionError as ex:
#   print(f'ZeroDivisionError: {ex} | {ex.__class__}')
# except Exception as ex:
#   print(f'Exception: {ex} | {ex.__class__}')
#   # pass
# else:
#   print(f'else é {x}')
# finally:
#   print('desnecessário')

# def contador(i, f, p):
#   '''
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#   '''
#   c = i
#   while c <= f:
#     print(f'{c}', end='...')
#     c += p
#   print('FIM!')

# contador(2, 10, 2)
# help(contador)


# def somar(a, b, c=0):
#   '''
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: o primeiro valor
#     :param b: o segund valor
#     :param c: o terceiro valor
#     Author:
#   '''
#   s = a + b + c
#   print(f'A soma vale {s}')

# somar(3, 2, 5)
# somar(8, 4)

# print('=-' * 30 + '=')
# help(system)
# print('=-' * 30 + '=')
# print(system.__doc__)
# print('=-' * 30 + '=')


# def teste(b):
#   global a, c
#   a = 8
#   b += 4
#   c = 2
#   print(f'a dentro={a}')
#   print(f'b dentro={b}')
#   print(f'c dentro={c}')

# a = 5
# teste(a)
# print(f'a={a}')
# print(f'c={c}')


# l = [3]
# l.insert(0, 2)
# print(l)

# lanche = ['a', 'b', 'c', 'd']
# print(lanche)
# lanche.append('e')
# print(lanche)
# lanche.insert(0,'x')
# print(lanche)

# del(lanche[0])
# print(lanche)
# lanche.pop()
# print(lanche)
# lanche.pop(1)
# print(lanche)
# lanche.insert(0,'a')
# print(lanche)
# lanche.remove('a')
# print(lanche)
# lanche.remove('a')
# print(lanche)

# l = []
# l.append(5)
# l.append(9)
# l.append(4)
# print(l)
# print(' '.join(f'{c}' for c in l))

# b = l
# # b = list(l)
# # b = l[:]
# b[1] = 3
# print(l)
# print(b)
# # print(b.index(9))

# lanche = range('a', 'd')
# print(lanche)


# # formata casas decimais
# val = 12.3
# print(f'{val:.2f}')
# print(f'{val:.5f}')

# # tabulação
# for x in range(1, 11):
#     print(f'{x:02} {x*x:3} {x*x*x:4} {x:05}')

# # alinhamento
# s1 = 'a'
# s2 = 'ab'
# s3 = 'abc'
# s4 = 'abcd'
# print(f'{s1:>10}')
# print(f'{s2:>10}')
# print(f'{s3:>10}')
# print(f'{s4:>10}')
# print(f'{s2:.>10}')

# # notação
# a = 300
# print(f"{a:x}") # hexadecimal
# print(f"{a:o}") # octal
# print(f"{a:e}") # scientific

# # horário
# from datetime import datetime
# now = datetime.now()
# print(f'{now:%Y-%m-%d %H:%M}')

# l1 = ["eat","sleep","repeat"]
# s1 = "geek"

# # creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)

# print ("Return type:", type(obj1))
# print ("Return type:", type(obj2))
# print (obj1)
# print (list(obj1))

# # changing start index to 2 from 0
# print (list(enumerate(s1, 2)))


# l1 = ["eat","sleep","repeat"]

# # printing the tuples in object directly
# for ele in enumerate(l1):
# 	print (ele)
# print
# # changing index and printing separately
# for count,ele in enumerate(l1,100):
# 	print (count, ele)


# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(sorted(lanche))

# # lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita']
# # print(sorted(lanche))

# for comida in lanche:
#   	print(f'Eu vou comer {comida}')

# for i in range(len(lanche)):
#   	print(f'Eu vou comer {lanche[i]} na posição {i}')

# for i, comida in enumerate(lanche):
#   	print(f'Eu vou comer {comida} na posição {i}')

# a = 1
# b = 2
# c = 3
# d = 4
# x = (a, b, c, d)
# print(x)

# first = ["axx", "bxx", "cxxxxxx"]
# second = ["dxxy", "eyxx", "fxxxxxyyx"]
# third = ["gxxzz", "hzxzx", "ixzxxxxx"]

# for one, two, three in zip(first, second, third):
#     print(one, two, three)

# for count, (one, two, three) in enumerate(zip(first, second, third)):
#     print(count, one, two, three)

# import sys
# import pygame
# from pygame.locals import *

# pygame.init()
# clock = pygame.time.Clock()
# clock.tick(60)
# pygame.mixer.music.load('/storage/emulated/0/qpython/curso_em_video/mundo_1/file_example_MP3_1MG.mp3')
# pygame.quit()

# print('hello')

# import unicodedata
# import re

# def remove_non_ascii_0(string: str) -> str:
#   return string.encode('ascii', 'ignore').decode('utf8')#.casefold()

# def remove_non_ascii_1(string: str) -> str:
#   normalized = unicodedata.normalize('NFD', string)
#   return normalized.encode('ascii', 'ignore').decode('utf8')#.casefold()

# def remove_non_ascii_2(string: str) -> str:
#   normalized = unicodedata.normalize('NFD', string)
#   return re.sub(r'[\u0300-\u036f]', '', normalized)#.casefold()

# def remove_non_ascii_3(string: str) -> str:
#   normalized = unicodedata.normalize('NFD', string)
#   return ''.join([c for c in normalized if not unicodedata.combining(c)])#.casefold()


# if __name__ == "__main__":
#   
#   string = 'Atenção \N{SNAKE}'
#   print(string)
#   # print([ord(c) for c in string])
#   # for x in [(c, f'U+{ord(c):04x}', unicodedata.name(c)) for c in string]:
#   #   print(x)
#   print(remove_non_ascii_0(string))
#   print(remove_non_ascii_1(string))
#   print(remove_non_ascii_2(string))
#   print(remove_non_ascii_3(string))
#   print(unicodedata.normalize('NFKD', string).encode('ASCII','ignore').decode('ASCII'))




# import timeit

# def in_(s, other):
#     return other in s

# def contains(s, other):
#     return s.__contains__(other)

# def find(s, other):
#     return s.find(other) != -1

# def index(s, other):
#     try:
#         s.index(other)
#     except ValueError:
#         return False
#     else:
#         return True



# perf_dict = {
#   'in:True': min(timeit.repeat(lambda: in_('superstring', 'str'))),
#   'in:False': min(timeit.repeat(lambda: in_('superstring', 'not'))),
#   '__contains__:True': min(timeit.repeat(lambda: contains('superstring', 'str'))),
#   '__contains__:False': min(timeit.repeat(lambda: contains('superstring', 'not'))),
#   'find:True': min(timeit.repeat(lambda: find('superstring', 'str'))),
#   'find:False': min(timeit.repeat(lambda: find('superstring', 'not'))),
#   'index:True': min(timeit.repeat(lambda: index('superstring', 'str'))),
#   'index:False': min(timeit.repeat(lambda: index('superstring', 'not'))),
# }

# for p in perf_dict:
#   print(p)






