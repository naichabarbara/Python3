'''
O presente arquivo contem apenas comentários parasuporte no aprendizado da linguagem Python
'''

'''
Quando alocadas dentro de uma váriavel, as cadeias de textos (strings) são divididas pelas suas letras, 
cada uma correspondendo a 1 índice que inica de zero a um número finito:

        exemplo:  'Python' separado em 6 indices (quantidade de suas letras) que vai de 0 a 5 (total 6)
'''

#FATIAMENTO - para exibir/trabalhar com partes especificas da string
frase = 'Programando em Python'
print(frase[9]) #retorna apenas a letra correspondente ao índice especificado -- no caso o Digite
print(frase[8:11]) #retorna letras dos indices 8,9 e 10 -- exclui o ultimo indice delimitador
print(frase[0:11:2]) #retorna os indices 0,3,5,7,9 - ultimo valor (2) indica o intervalo de indices
print(frase[:5]) #começa do indice zero (já que não foi especificado) e termina no indice 5
print(frase[0:]) #oposto do exemplo acima so especificando o começo


#ANÁLISE - para exibir/trabalhar com caracteristicas da string
print(len(frase)) #exibe o comprimento da frase
print(frase.count('o')) #conta quantas letras 'o' (minúsculas) tem na frase
print(frase.find('mando')) #retorna indice inicial da parte especificada do texto
                    #caso seja passado um valor não encontrado pelo o .find, o valor retornado será -1
print('Python' in frase) #retorna true para se encontrado a frase or false para caso não encontrado


#TRANSFORMAÇÃO DE STRINGS - Muda caracteristicas de Strings
frase.replace('Python', 'Android') #altera a palavra Python para Android
                                #salva a alteração se for armazenada em uma váriavel
frase.upper() #transforma todas as letras em caixa alta
frase.captalize() #transforma só o primeiro caracter em maiúsculo
frase.title() #transforma todos os caracteres inicias (de palavras) em maiúsculo
frase.strip() #remove espaços ínuteis no começo e no final da string
        # --> variações com rstrip() que remove apenas do lado direito e lstrip() para o lado esquerdo


#DIVISÃO - dividir partes da string para que sejam manipuladas separadamente
frase.split() #faz a divisão das strings pelos espaços em branco:
        #chão sujo (9 indices - 0 a 8), com o split passa a ser duas listas(0 e 1) com 4 indices (0 a 3)
'-'.join(frase) #faz a junção das listas, separadas a cima, com separador '-'
