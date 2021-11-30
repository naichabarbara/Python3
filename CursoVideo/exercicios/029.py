'''
Leia a velocidade de um carro e se ele ultrapassar de 80km mostre uma mensagem de multa com o valor
(a multa deve valer R$ 7,00 por km acima do limite) 
'''

print('**** Verifique o status da multa por alta velocidade ****')
print('É aplicado a multa de R$ 7.00 por kilometragem acima do limite\n')
km = int(input('Qual velocidade foi registrada pelo o radar?: '))

if km > 80:
    km = (km - 80) * 7
    print('O motorista deverá pagar uma multa de R$ {:.2f} \U0001F6A8'.format(float(km)))
else:
    print('{}km está abaixo da velocidade limite e não receberá multa! \U0001F44F'.format(km))

print('\n**** FIM ****')