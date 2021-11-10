'''
Um professor quer um voluntário para apagar a lousa. Sorteie um nome (aleatório) para fazer o trabalho 
'''

import random

print('*** Sorteie um dos nomes cadastrados ***\n')

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o último nome: ')

print('\nO nome sorteado para apagar a lousa é o(a) {}!'.format(random.choice([n1, n2, n3, n4])))
#lista fica entre CONCHETES

print('\n*** FIM ***')

