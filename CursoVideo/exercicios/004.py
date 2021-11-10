'''
Faça um programa que leia algo digitado pelo o usuário e mostre seu tipo primitivo e todas informações
possíveis (utilizando .is - teste de tipo)
'''

print('***Descubra as caracteristicas de algo digitado***')
objeto = input('Digite algo [seja criativo(a)]: ')

print(f'\nO tipo primitivo de \'{objeto}\' é', type(objeto), sep=" = ")
#comandos a seguir com respostas apenas em True or False
print('\nSó tem espaços?', objeto.isspace(), sep=" = ")
print(f'\'{objeto}\' é alfanumérico?', objeto.isalnum(), sep=" = ")
print(f'\'{objeto}\' é composto por números?', objeto.isnumeric(), sep=" = ")
print(f'\'{objeto}\' é alfabético?', objeto.isalpha(), sep=" = ")
print(f'\'{objeto}\' tem todas as letras em caixa BAIXA?', objeto.islower(), sep=" = ")
print(f'\'{objeto}\' tem todas as letras em caixa ALTA?', objeto.isupper(), sep=" = ")
print(f'\'{objeto}\' está captalizada?', objeto.istitle(), sep=" = ")

print('*** FIM ***')
