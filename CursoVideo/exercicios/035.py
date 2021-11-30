'''
Leia o comprimento de três retas e informe se elas podem ou não formar um triângulo
'''

print('\U0001F53A Forme um triângulo através da medida de três retas \U0001F53A\n')

reta1 = int(input('Valor da primeira reta: '))
reta2 = int(input('Valor da segunda reta: '))
reta3 = int(input('Valor da última reta: '))

    
if ((reta1 + reta2) > reta3) and ((reta1 + reta3) > reta2) and ((reta2 + reta3) > reta1):
    print('\nCom as medidas passadas, É POSSÍVEL fazer um triângulo!')
else:
    print('\nCom as medidas passadas, NÃO É POSSÍVEL fazer um triângulo')
    
print('\n**** FIM ****')