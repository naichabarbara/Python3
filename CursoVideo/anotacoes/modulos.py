'''
O presente arquivo contem apenas comentários parasuporte no aprendizado da linguagem Python
'''

#O comando import é utilizado para incluir ao Python bibliotecas e funcionalidades adicionais
    # import{biblioteca} --> importa todas as funcionalidades da biblioteca
    # from{biblioteca}import{funcionalidade} --> para importar funcionalidade especifica
    
import math    #faz a importação da biblioteca de matemática

num = int(input('Digite um número: '))
num = math.sqrt(num)  #para calcular a raiz quadrada
print(num)

#Ou pode ser importado apenas a funcionalidade especifica

from math import sqrt   #faz importação apenas da função de raiz quadrada

num = int(input('Digite um número: '))
num = sqrt(num) #não precisa invocar o 'math'
print(num)

# DOCUMENTAÇÃO COM COMANDOS MATH: https://docs.python.org/pt-br/3/library/math.html

import random   #biblioteca de números aleatórios

num = random.randint(0, 1000)  #sorteia um número aleatório de zero a mil
print(num)

#códigos de emojis pode ser consultado em: https://apps.timwhitlock.info/emoji/tables/unicode
#todos devem substituir o sinal + por 000 e acrescentar barra a frente
print('\U0001F601') 
