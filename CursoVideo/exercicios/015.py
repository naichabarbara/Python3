'''
Pergunte a quantidade de quilometros percorridos e quantidade de dias de aluguel do carro. 
Sabendo que o aluguel do carro custa R$60/dia e R$0.15/km rodado, calcule o total a pagar
'''

print('*** Calcule o valor total do aluguel de carro ***\n')

dia = int(input('Quantos dias o carro ficou em posse do(a) cliente?: '))
km = float(input('Quantos kilometros foram rodados por ele(a) durante esses dias?: '))


print('\nCom {} dias de posse e {} km rodados, o(a) cliente deve pagar: R${:.2f}'.format(dia, km, ((dia * 60) + (km * 0.15))))
print('\n*** FIM ***')
