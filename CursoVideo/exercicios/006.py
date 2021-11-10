'''
Faça um programa que leia um número e mostre seu dobro, triplo e raiz quadrada
'''

print('*** Calcule o dobro, triplo e raiz quadrada de um número inteiro qualquer ***\n')

numero = int(input('Digite um número: '))

print('O DOBRO de {} = {}'.format(numero, (numero * 2)))
print('O TRIPLO de {} = {}'.format(numero, (numero * 3)))
print('RAIZ QUADRADA de {} = {:.2f}'.format(numero, (numero ** 0.5)))

print('\n*** FIM ***')
