'''
Escreva um programa que sorteie um número inteiro de 0 a 5 e faça o usuário adivinhar o número. Ao final
informe se o usuário venceu ou perdeu!
'''
import random
import time

print('\U0001F52E JOGO DE ADIVINHAÇÃO \U0001F52E\n')
print('{:>5}{}{}'.format('+', '-' * 15, '+')) 
print(f"{'Tente adivinhar':^25}\n{'o número secreto':^24}\n{'entre 0 e 5!':^25}")
print('{:>5}{}{}'.format('+', '-' * 15, '+'))

num = random.randint(0, 5) #escolha aleatória ente 0 e 5
escolha = int(input('\nQual número você aposta?: '))

if escolha == num:
    print('\nVerificando...')
    time.sleep(2) #faz o computador aguardar 2 segundos antes de mostrar a resposta
    print('\PARABÉNS! VOCÊ GANHOU \U0001F389\nO número secreto é o {}!'.format(escolha))
else:
    print('\nVerificando...')
    time.sleep(2)
    print('\nVOCÊ PERDEU \U0001F61E\nO número secreto era o {}!'.format(num))

print('\n**** FIM ****') 
