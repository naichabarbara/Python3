'''
Leia três números inteiros e informe qual é o maior e qual é o menor
'''

print('**** Veja o maior e menor valor de um sequência de números ****\n')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Agora, o segundo número: '))
num3 = int(input('E o último número: '))


if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
elif num3 >= num1 and num3 >= num2:
    maior = num3

print('\nMAIOR VALOR da sequência: {}'.format(maior))


if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
elif num3 <= num1 and num3 <= num2:
    menor = num3

print('MENOR VALOR da sequência: {}'.format(menor))
print('\n**** FIM ****')


#SIMPLIFICADO (ideia de outro aluno):

'''
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))
'''
