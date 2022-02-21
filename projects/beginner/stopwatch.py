#Created in: 07/02/2022
#By: Barbara Naicha
#github: https://github.com/naichabarbara

import time
import pygame

def count(x):
    for x in range(0, x+1):
        m, s = divmod(x, 60)
        min_sec = '{:02d}:{:02d}'.format(m, s)
        print(min_sec)
        time.sleep(1)
        
    pygame.init() #inicializar o pygame
    pygame.mixer.music.load('stopwatch.mp3')
    pygame.mixer.music.play()
    print('\033[36mCOUNT IS OVER!\033[m')

print('\U0001F550 Don\'t waste your time \U0001F550\n')		
sec = int(input('Time to be counted in seconds [for instance: 120 for 2 minutes] '))
count(sec)

def restart():
    resp = input('\n\033[31mInsert [1] to count again\033[m ')
    if resp == '1':
        count()
        restart()
    else:
        print('Bye....')
        time.sleep(1)
        exit()

restart()
