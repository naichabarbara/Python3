#Created in: 07/02/2022
#By: Barbara Naicha
#github: https://github.com/naichabarbara

import random
import time
import getpass

def game():
    print('\033[32m+{:^15}+'.format('-'*20))
    print('|{:^20}|'.format('GAME TIME!'))
    print('+{:^15}+\033[m'.format('-'*20))
	
    print('\n\U0001F6A8 I dare you to a game of JOKENPÔ \U0001F6A8')
    ans = getpass.getpass('\033[31mInsert [1] to accept \033[m')
    
    if ans != '1':
        print('\nThat\'s to bad \U0001F610 \nTake care, friend!')
        exit()
    else:
        list = ['rock', 'paper', 'scissors']

        print('\nI will play first \n \033[;7mchoosing...\033[m')
        mach = random.choice(list)
        time.sleep(2)
        print('I made my choice \U0001F61B')

        player = input('\nIt\'s your time! You will play... ').lower()
    
        #validate input
        x = 0
        while (player != 'rock' and x < 2) and (player != 'paper' and x < 2) and (player != 'scissors' and x < 2):
            player = input('ERROR! Choose between rock, paper or scissors: ')
            x += 1
            if x > 2:
                print('\nGame Over!')

        #result
        if player == mach:
            print('You read my mind \U0001F4AC \nYou choose {} and I {}'.format(player, mach))
        else:
            if (player == 'scissors' and mach == 'paper') or (player == 'paper' and mach == 'rock') or (player == 'rock' and mach == 'scissors'):
                print('WINNER \U0001F389 \nYou choose {} and I {}!'.format(player, mach))
            elif (mach == 'scissors' and player == 'paper') or (mach == 'paper' and player == 'rock') or (mach == 'rock' and player == 'scissors'):
                print('LOSER \U0001F61C \nYou choose {} and I {}'.format(player, mach))
            else:
                print('\nThere\'s no winners!!')
			
game()

def restart():  
    resp = getpass.getpass('\n\033[31mInsert [1] to restart \033[m\n')
    if resp == '1':
        game()
        restart()
    else:
        print('I hope you liked it! Bye \U0001F49C')
        exit()

restart()
