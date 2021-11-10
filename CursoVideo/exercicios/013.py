'''
Faça um programa que leia o salário de um funcionário e reajuste o valor com 15% a mais
'''

print('*** Reajuste de 15% no salário ***\n')

salario = float(input('Digite o valor do salário atual: '))

print('Com reajuste de 15%, o salário de R${} passa a valer R${:.2f}'.format(salario, (salario * 1.15)))
print('\n*** FIM ***')
