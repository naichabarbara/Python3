'''
Pergunte a distância de uma viagem em km. Calcule o preço da viagem sendo R$0,50 (km) para viagens de até 
200km e R$0,45 para viagens mais longas
'''

print('**** Calcule o preço da passagem ****\n')
km = int(input('Qual a distância [em kilometros] da viagem?: '))

if km <= 200:
    print('Para viagem de {}km a passagem custa R$ {:.2f}'.format(km, (km * 0.50)))
else:
    print('Para viagem de {}km a passagem custa R$ {:.2f}'.format(km, (km * 0.45)))

print('\n**** FIM ****')   
