'''
O presente arquivo contém apenas comentários e trechos de códigos para apoio no aprendizado da linguagem Python!
'''

#comentário de uma linha --> cerquilha
#comentário de várias linhas --> três aspas

'''
Strings devem ser digitas acompanhadas de aspas, dupla ou simples

OBS: tudo que é digitado no 'input' segue como string, para mudar o tipo 
do dado, deve colocar a informação a frente do comando: ex --> int(input('valor'))

Não há limitadores e o controle de blocos é feito pela a indentação
'''
#Boas práticas: NÃO colocar espaço entre função e comando

print('Olá, mundo!')
print(7 + 4) #faz a soma dos números
print('7' + '4') #por estar em formato de string, faz a JUNÇÃO dos dois números

#não é necessário criar váriaveis no topo do código com os tipos
nome=input('\nDigite o seu nome: ')
idade=input('Digite sua idade: ')
profissao=input('Qual a sua profissão: ')

print()
print('Nome: ', nome, '\nidade: ', idade, '\nprofissão: ', profissao) #\n para pular linha

print('\nFim do programa')


#leia o nome da pessoa e dê boas-vindas com o dado informado

nome=input('\nOlá, digite o seu nome: ')
print('Seja bem-vindo(a), {}'.format(nome)) #outra maneira de referenciar váriaveis

print('\nFim do programa')


#leia o dia, mes e ano de nascimento do usuário e retorne os valores formatados

dia=input('Digite o dia que você nasceu: ')
mes=input('Agora, o mês: ')
ano=input('E o ano: ')
print('\nVocê nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')


#leia dois números e mostre a soma entre eles

print('*** Some dois valores ***')
num1=int(input('Digite um número: '))
num2=int(input('Digite outro número: '))

print('\nA soma dos dois números é igual a: ', num1 + num2)

print('\nFim do programa')