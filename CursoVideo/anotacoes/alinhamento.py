'''
O presente arquivo contém apenas comentários e trechos de códigos para apoio no aprendizado da linguagem Python!
'''

#com o .format é possivel fazer alinhamento do dado da variável:

nome = input('Digite seu nome: ')
print('Prazer em te conhecer {:<20}'.format(nome)) #alinha a esquerda
print('Prazer em te conhecer {:>20}'.format(nome)) #alinha a direita
print('Prazer em te conhecer {:^20}'.format(nome)) #centraliza
print('Prazer em te conhecer {:=^20}'.format(nome)) #centraliza com sinais de igual em volta

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
divisao = n1 / n2
print('A divisão é {:.3f}'.format(divisao)) #:.3f arredonda para três casas flutuantes