'''
Leia um ano e informe se é ano bissexto ou não
'''
import datetime

print('**** Descubra se o ano é bissexto ou não ****\n')
ano = int(input('Qual ano você deseja consultar? [digite 0 para verificar o ano atual]: '))

if ano == 0:
    ano = datetime.date.today().year #verifica a data atual através da máquina e retorna apenas o ano [.year]
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print('{} É um ano bissexto!'.format(ano))
else:
    print('{} NÃO É um ano bissexto!'.format(ano)) 

print('\n**** FIM ****')
