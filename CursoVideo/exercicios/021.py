'''
Faça um programa que abra e leia um arquivo MP3
'''

import pygame
pygame.init() #faz a inicialização do pygame

#documentação do pygame é encontrada em: https://www.pygame.org/docs/

pygame.mixer.music.load('021.mp3') #carrega o arquivo MP3 que está na mesma pasta do script
pygame.mixer.music.play() 
pygame.event.wait()

