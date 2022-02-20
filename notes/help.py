'''
O presente arquivo contém apenas comentários e trechos de códigos para apoio no aprendizado da linguagem Python!
'''

#PROGRAMAÇÃO DE ALTO NÍVEL: Linguagem mais próxima da linguagem humana;
#PROGRAMAÇÃO DE BAIXO NÍVEL: Linguagem mais próxima da linguagem de computadores.

#!!Inputs são strings por padrão!!

#Váriaveis podem ser criadas diretamente no input e/ou terem valores já declarados
	nome = input('Digite seu nome: ')
#São úteis para armazenar resultados de alguma operação para que possa ser usado em outros pedaços do código


#Se usa o sinal de adição '+' para concatenar strings e sinal de multiplicação '*' para multiplicar strings
	print('Bem-vindo' + 'nome')
	print('nome' * 3)


'''
Pode-se converter o tipo de um dado da seguinte maneira

str()   --> para converter em string
int()   --> para converter em inteiro
float() --> para converter em numero real
'''

#CÓDIGOS DE EMOJIS: https://apps.timwhitlock.info/emoji/tables/unicode --> substituir  + por 000 e acrescentar barra a frente
print('\U0001F601') 


#FUNCÕES INICIAIS

#pow(4,3) #corresponde a 4 elevado a 3
#min() retorna o MENOR valor dentro de um intervalo de dados
#max() retorna o MAIOR valor dentro de um intervalo de dados

print(0o123) #se o número for precedido por 0o ele será tratado como um valor octal (sistema base 8)
print(0x123) #0x para tratar de numeros hexadecimais (sistema base 16)
print('A divisão é {:.3f}'.format(divisao)) #:.3f arredonda para três casas flutuantes
print("Programming", "Essentials", "in", sep="**", end="-\n") #sep --> separador de argumentos  /  end --> como o determinado print deve ser terminado


#ALINHAMENTO

nome = input('Digite seu nome: ')
print('Prazer em te conhecer {:<20}'.format(nome)) #alinha a esquerda
print('Prazer em te conhecer {:>20}'.format(nome)) #alinha a direita
print('Prazer em te conhecer {:^20}'.format(nome)) #centraliza
print('Prazer em te conhecer {:=^20}'.format(nome)) #centraliza com sinais de igual em volta


#MANIPULANDO LISTA E STRINGS
#TODA STRING/LISTA COMEÇA DO INDICE 0

frase = 'Programando em Python'
print(frase[9]) #retorna apenas a letra correspondente ao índice especificado -- no caso o Digite
print(frase[8:11]) #retorna letras dos indices 8,9 e 10 -- exclui o ultimo indice delimitador
print(frase[0:11:2]) #retorna os indices 0,3,5,7,9 - ultimo valor (2) indica o intervalo de indices
print(frase[:5]) #começa do indice zero (já que não foi especificado) e termina no indice 5
print(frase[0:]) #oposto do exemplo acima so especificando o começo

print(len(frase)) #exibe o comprimento da frase
print(frase.count('o')) #conta quantas letras 'o' (minúsculas) tem na frase
print(frase.find('mando')) #retorna indice inicial da parte especificada do texto
                    #caso seja passado um valor não encontrado pelo o .find, o valor retornado será -1
print('Python' in frase) #retorna true para se encontrado a frase or false para caso não encontrado

frase.replace('Python', 'Android') #altera a palavra Python para Android
                                #salva a alteração se for armazenada em uma váriavel
frase.upper() #transforma todas as letras em caixa alta
frase.lower() #transforma todas as letras em caixa baixa
frase.captalize() #transforma só o primeiro caracter em maiúsculo
frase.title() #transforma todos os caracteres inicias (de palavras) em maiúsculo
frase.strip() #remove espaços ínuteis no começo e no final da string
        # --> variações com rstrip() que remove apenas do lado direito e lstrip() para o lado esquerdo

frase.split() #faz a divisão das strings pelos espaços em branco:
'-'.join(frase) #faz a junção das listas, separadas a cima, com separador '-'



#CORES NO TERMINAL
print("\033[31mTESTE")

#CÓDIGO PADRÃO USADO PARA CORES: \033[ {código da cor} m    //   linkpara códigos > https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/

9 - 29 - 
