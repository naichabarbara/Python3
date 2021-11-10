'''
Faça um programa que leia o cateto oposto e cateto adjacente e calcule o valor da hipotenusa
    --> utilizar biblioteca math
'''

from math import hypot

print('*** Calcule o valor da hipotenusa ***\n')

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))


print('\nO valor da hipotenusa = {:.2f}'.format(hypot(adjacente, oposto)))
print('\n*** FIM ***')

