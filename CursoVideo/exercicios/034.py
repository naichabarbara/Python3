'''
Leia o salário de um funcionário e calcule o valor do aumento - para salários de até R$1.250 o aumento é de
15%, para os demais o aumento é de 10%
'''

print('\U0001F4B2 REAJUSTE DE SALÁRIO \U0001F4B2\n')
salario = float(input('Valor atual do salário: '))

if salario <= 1250:
    print('Com o reajuste de 15% o salário passa de R$ {:.1f} para R$ {:.1f}'.format(salario, (salario * 1.15)))
else:
    print('Com reajuste de 10% o salário passa de R$ {:.1f} para R$ {:.1f}'.format(salario, (salario * 1.10)))

print('\n**** FIM ****')
