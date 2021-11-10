'''
Faça um programa que leia um preço e retorne o novo preço com 5% de desconto
'''

print('*** Ganhe 5% de desconto ***\n')
valor = float(input('Digite o valor do produto: '))

print('Com desconto de 5%, o produto de R${} passa a valer: R${:.2f}'.format(valor, (valor * 0.95)))
print('\n*** FIM ***')
