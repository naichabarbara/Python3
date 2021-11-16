'''
Crie um programa que leia o nome de uma cidade e se ela começa ou não com a palavra 'Santo'
'''

print('*** O programa identfica se o nome da cidade começa com \'Santo\'\n')
cidade = input('Digite o nome de uma cidade: ')

cidade = cidade.strip()
cidade = cidade.split()

if cidade[0] == 'Santo' or cidade[0] == 'santo':
    print('O nome da cidade \'{}\' começa com a palavra \'Santo\''.format(' '.join(cidade)))
else:
    print('O nome da cidade \'{}\' não começa com a palavra \'Santo\''.format(' '.join(cidade)))
   
    
print('\n*** FIM ***')
