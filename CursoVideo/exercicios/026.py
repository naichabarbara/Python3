'''
Leia uma frase e mostre: 
    quantas vezes aparece a letra 'A'
    em que posição ela aparece a primeira vez
    em que posição ela aparece a última vez
'''

print('*** Encontrando o caracter \'A\' em uma frase ***\n')
frase = input('Digite uma frase qualquer: ').upper().strip()


print('A letra \'A\' aparece {}x na frase!'.format(frase.count('A')))
print('O primeiro índice da letra \'A\' na frase é o índice {}'.format(frase.find('A') + 1)) 
print('O último índice da letra \'A\' é o índice {}'.format(frase.rfind('A') + 1))

#'+1' reorganiza as posições do Python para começar como indice 1

print('\n*** FIM ***')

