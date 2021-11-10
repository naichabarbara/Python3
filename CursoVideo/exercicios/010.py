'''
Crie um programa que leia um valor em reais e mostre quantos dólares pode ser comprado com aquela quantia
    considerando o dólar por R$ 3,27
'''
print('*** Saiba quantos dólares consegue comprar ***\n')
real = float(input('Digite quanto você tem em real: '))

print('Com R${:.2f} você pode comprar US${:.2f}!'.format(real, (real / 3.27)))
print('\n*** FIM ***')
