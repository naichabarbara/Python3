'''
Crie um programa que leia o nome de uma cidade e se ela começa ou não com a palavra 'Santo'
'''

print('*** O programa identfica se o nome da cidade começa com \'Santo\'\n')
cidade = input('Digite o nome de uma cidade: ').strip()

cidade = cidade.title() #para deixar nomes prórios com letras maiúsculas
cidade = cidade.split()


if cidade[0].upper() == 'SANTO':
    print('A cidade \'{}\' COMEÇA com a palavra \'Santo\''.format(' '.join(cidade)))
else:
    print('A cidade \'{}\' NÃO COMEÇA com a palavra \'Santo\''.format(' '.join(cidade)))
   
    
print('\n*** FIM ***')
