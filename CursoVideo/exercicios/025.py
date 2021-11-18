'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
'''

print('*** O programa identifica se um nome possuí \'Silva\'\n')
nome = input('Digite um nome completo: ').strip()

nome = nome.upper()

if nome.find('SILVA') != -1:
    print('O nome \'{}\' TEM sobrenome \'Silva\''.format(nome.title()))
else:
    print('O nome \'{}\' NÃO TEM sobrenome \'Silva\''.format(nome.title()))
  
print('\n*** FIM ***')



#RESOLUÇÃO DO PROFESSOR 

'''
nome = input('Digite um nome completo: ')
print('Seu nome tem silva?'.format('silva' in nome.lower()))
'''