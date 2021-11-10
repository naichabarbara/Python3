'''
Faça um program que converta a temperatura de Celsius para Fahrenheit
'''
print('*** Converta Celsius em Fahrenheit ***\n')
celsius = float(input('Digite a temperatura em ºC: '))

print('Em Fahrenheit, {:.1f}ºC equivale a: {:.1f}ºF'.format(celsius, (celsius * 1.8 + 32)))
print('\n*** FIM ***')

#para converter o oposto a fórmula é: (fahrenheit - 32) / 1.8