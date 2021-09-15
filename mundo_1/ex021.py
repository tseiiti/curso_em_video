from os import system, name
system('cls' if name == 'nt' else 'clear')

dsc = ('''DESAFIO 021:
Faça um programa em Python que abra e reproduza o áudio de um
arquivo MP3.
''')

from pygame import mixer
mixer.init()
mixer.music.load('file_example_MP3_1MG.mp3')
mixer.music.play()

# foi necessario colocar esse input
input('Pressione [ ENTER ] para parar...')

# import androidhelper
# droid = androidhelper.Android()
# file = '/storage/emulated/0/qpython/curso_em_video/file_example_MP3_1MG.mp3'
# droid.mediaPlay(file)
