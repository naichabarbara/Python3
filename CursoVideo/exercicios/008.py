'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''

print('*** Converta metros em centímetros e milímetros ***')
met = float(input('Digite uma distância em metros: '))

print('\n{} metros convertido em centímetros = {:.2f}cm'.format(met,(met * 100)))
print('{} metros convertido em milímetros = {:.2f}mm'.format(met, (met * 1000)))
print('{} metros convertido em decímetros = {:.2f}dm'.format(met, (met * 10)))
print('{} metros convertido em kilometros = {:.2f}km'.format(met, (met / 1000)))
print('{} metros convertido em hectómetros = {:.2f}hm'.format(met, (met / 100)))
print('{} metros convetido em decâmetros = {:.2f}dam'.format(met, (met / 10)))

print('\n*** FIM ***')
