'''
Faça um programa que leia um ângulo qualquer e retorne o valor de seno, cosseno e tangente
'''

from math import sin, cos, tan, radians

print('*** Calcule o seno, cosseno e tangente de uma medida ***\n')

medida = float(input('Digite a medida desejada: '))

#a medida tem que ser convertida em radianos para que seja feito o calculo da maneira correta
print('\nO seno de {}º = {:.2f}'.format(medida, sin(radians(medida))))
print('O cosseno de {}º = {:.2f}'.format(medida, cos(radians(medida))))
print('A tangente de {}º = {:.2f}'.format(medida, tan(radians(medida))))

print('\n*** FIM ***')
