"""
EXERCÍCIO 021: Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""


import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()


'''from pygame import mixer
from time import sleep
musica = 'ex021.mp3'
mixer.init()
mixer.music.load(musica)
mixer.music.play()
sleep(120)'''
