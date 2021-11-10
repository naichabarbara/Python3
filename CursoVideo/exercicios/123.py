'''
Escreva um programa que imprima "Olá, mundo!" no ecrã
'''

print('Olá, mundo!') #NÃO coloca espaço entre função e parâmetro

'''
Crie um programa que dê 'boas-vindas' com o nome digitado pelo o usuário
'''

nome = input('Olá! digite o seu nome: ')
#print('Seja bem-vindo (a), ', nome)
print('Seja bem-vindo(a), {}'.format(nome)) #outro tipo de formatação

'''
Faça um programa que solicite dois números e mostre a soma entre eles
'''

n1 = int(input('Digite um número: ')) #converte para inteiro para que possa ser feita a soma
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma entre {} e {} vale {} - .format'.format(n1, n2, soma))
print(f'A soma entre {n1} e {n2} vale {n1 + n2} - f-string') #NÃO é necessário variável de soma


'''
é possivel saber o tipo do dado inserido com 'print(type({valor}))' 
também pode usar o .is..para saber o tipo da variável (por true or false):

n = 123
print(n.isalnum)

tem como resultado FALSE pois não é um valor alfanumérico
'''
