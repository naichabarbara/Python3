'''
Crie um programa que leia um número real e mostre na tela a sua parte inteira
'''
from math import trunc

print('*** Veja a parte inteira de um número real ***\n')

numero = float(input('Digite um número real: '))
print('O número {} tem parte inteira {}'.format(numero, trunc(numero)))
#pode ser feito com as funções int e floor da biblioteca 'math'

print('\n*** FIM ***')