'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
'''

print('*** O programa identifica se um nome possuí \'Silva\'\n')
nome = input('Digite um nome completo: ')

nome = nome.strip()
nome = nome.title()

if nome.find('Silva') != -1:
    print('O nome \'{}\' tem sobrenome \'Silva\''.format(nome))
else:
    print('O nome \'{}\' não tem sobrenome \'Silva\''.format(nome))
  
print('\n*** FIM ***')
