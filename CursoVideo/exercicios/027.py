'''
Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e último nome separadamente
'''

print('*** Mostre um nome completo separadamente ***\n')
nome = input('Digite um nome completo: ')

nome = nome.split()

print('O primeiro nome: {}'.format(nome[0]))
print('Último nome: {}')
