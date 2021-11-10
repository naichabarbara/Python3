'''
Faça um programa que leia a largura e altura de uma parede em metros, calcule a área e quantidade de tinta para pintar a parede
    considerando um litro para 2 metros quadrados
'''

print('*** Calcule quanto de tinta será usado para pintar a parede ***\n')
altura = float(input('Digite a altura [em metros] da parede: '))
largura = float(input('Digite a largura [em metros] da parede: '))

print('\nA área da parede {}x{} é igual {:.2f}m²'.format(altura, largura, (altura * largura)))
print('Será necessário {:.2f} litros de tinta para pintar a parede!'.format(((altura * largura) / 2)))

print('\n*** FIM ***')
