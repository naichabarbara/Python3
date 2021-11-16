'''
Leia uma frase e mostre: 
    quantas vezes aparece a letra 'A'
    em que posição ela aparece a primeira vez
    em que posição ela aparece a última vez
'''

print('*** Encontrando o caracter \'A\' em uma frase ***\n')
frase = input('Digite uma frase qualquer: ')


print('A letra \'A\' aparece {}x na frase {}'.format(frase.count('a' + 'A'), frase))
print('O primeiro índice da letra \'A\' na frase {} é o índice {}'.format(frase, frase.lower(frase.find('a'))))

