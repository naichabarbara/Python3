'''
Leia um número inteiro digitado pelo o usuário e informe se é um número par ou ímpar
'''

print('**** Digite um número e descubra se ele é par ou ímpar ****\n')
num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print('{} é um número PAR!'.format(num))
else:
    print('{} é um número ÍMPAR!'.format(num))

print('\n**** FIM ****')
