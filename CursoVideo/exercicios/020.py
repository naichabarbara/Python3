'''
O mesmo professor do exercicios anterior quer que agora seja sortada a ordem de apresentação dos 4 alunos
'''

import random

print('*** Sorteie a ordem de apresentação ***\n')

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o último nome: ')

lista = [n1, n2, n3, n4]

print('\nA ordem de apresentação será: {}'.format(random.sample([n1, n2, n3, n4], k=2)))
print('\nA ordem de apresentação será: {}'.format(random.shuffle(lista))) #usado pelo o prof
print('\n*** FIM ***')
