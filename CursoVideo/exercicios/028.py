'''
Escreva um programa que sorteie um número inteiro de 0 a 5 e faça o usuário adivinhar o número. Ao final
informe se o usuário venceu ou perdeu!
'''
import random

print('\U0001F52E JOGO DE ADIVINHAÇÃO \U0001F52E\n')
print('{:>5}{}{}'.format('+', '-' * 15, '+')) 
print(f"{'Tente adivinhar':^25}\n{'o número secreto':^24}\n{'entre 0 e 5!':^25}")
print('{:>5}{}{}'.format('+', '-' * 15, '+'))

num = random.randint(0, 5) #escolha aleatória ente 0 e 5
escolha = int(input('\nQual número você aposta?: '))

if escolha == num:
    print('\nPARABÉNS \U0001F389')
    print('O número secreto é o {}!'.format(escolha))
else:
    print('\nNÃO FOI DESSA VEZ \U0001F61E')
    print('O número secreto era o {}!'.format(num))

print('\n**** FIM ****') 
