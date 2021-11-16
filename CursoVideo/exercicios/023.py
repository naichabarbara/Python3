'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

        EXEMPLO: 1834  - unidade: 4 - dezena: 3 - centena: 8 - milhar: 1
'''

print('*** Descubra as casas decimais de um número inteiro ***\n')
num = (input('Por favor, digite um número entre 0 e 9999: '))

num = num.strip()
ponto = '.' in num

#validar que não tem nenhum número real e maior que 9999
while ponto == True or len(num) > 4: 
    num = input('!ERRO! Digite um número inteiro entre 0 e 9999: ')

    num = num.strip()
    ponto = '.' in num


if len(num) <= 4:
    if len(num) == 1:
        print('Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}'.format(num, 'nulo', 'nulo', 'nulo'))
        #exit()
    elif len(num) == 2:
        print('\n', '-' * 14, '\n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}\n'.format(num[1], num[0], 'nulo', 'nulo'), '-' * 14)
        #exit()
    elif len(num) == 3:
        print('\n', '-' * 14, '\n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}\n'.format(num[2], num[1], num[0], 'nulo'), '-' * 14)
        #exit()
    elif len(num) == 3:
        #print('\n', '-' * 14, '\n Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}\n'.format(num[3], num[2], num[1], num[0]), '-' * 14)
        exit()


    print('\n*** FIM ***')
