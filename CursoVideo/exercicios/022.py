'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras maiúsculas;
    O nome com todas ||   ||   minúsculas;
    Quantas letras ao todo (sem espaço);
    Quantas letras tem o primeiro nome.
'''

print('*** Manipulando um nome ***\n')
nome = input('Por favor, digite um nome completo: ').strip()


print('\nNome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Número total de caracteres que compõe o nome: {}'.format(len(nome.replace(" ", "")))) #substitui espaço por nada

nome = nome.split()
print('O primeiro nome é {} e tem {} letras!'.format(nome[0], len(nome[0])))

print('\n*** FIM ***')
