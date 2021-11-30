'''
Leia um ano e informe se é ano bissexto ou não
'''

print('**** Descubra se o ano é bissexto ou não ****\n')
ano = int(input('Qual ano você deseja consultar?: '))

if ano % 4 == 0:
   print('{} É um ano bissexto!'.format(ano))
else:
    print('{} NÃO É um ano bissexto!'.format(ano)) 

print('\n**** FIM ****')
