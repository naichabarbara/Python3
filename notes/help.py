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

list = [a, b, [c, d]] #criação de sublistas
#para 'puxar' apenas o item C, faremos da seguinte maneira
print(list[1][0])

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


#TUPLAS são basicamente listas imutáveis e para criá-las basta usar parenteses
lista = ('maça', 'pera', 'abacaxi')


#DICIONÁRIOS são represemtados por chaves '{}' e seus dados são compostos:
#nome/idade = chaves   joao/30 = valores    nome;joao = itens
a = {'nome':'joão', 'idade':30}
a['nome'] #retorna 'joão'
('nome', 'joão') in a.itens() #procura itens em um dicionário (tem que criar uma tupla para busca)
'nome' in a.keys() #modo de procurar chaves
'joão' in a.values() #modo de procurar valores
a['nome'] = 'maria' #muda um valor dentro do dicionário (tem que chamar pela a chave)
a['altura'] = 1.60 #adiciona um valor ao dicionário
del(a['nome']) #remove o nome da lista
copia = a.copy() #para copiar um dicionário sem fazer alteração no original
a.update(copia) #junta os dois dicionários



#CORES NO TERMINAL
print("\033[31mTESTE")
#CÓDIGO PADRÃO USADO PARA CORES: \033[ {código da cor} m    //   linkpara códigos > https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/


#EXPRESSÕES REGULARES
import re #biblioteca paratrabalhar com as expressões

string = 'É um teste'
re.search(r'teste', string) #encontra 'teste' na string e retorna o indice inic/fim da primeira palavra
re.findall(r'teste', string) #retorna todos os indices que forem encontrados a palavra 'teste'
re.sub(r'teste', 'ABC', string, count=1) #substitui uma palavra pela a outra (count é para substitir apenas um indice)

#compile pega a expressão regular e trata ela como uma váriavel para ser invocada com suas funções:
achar = re.compile(r'teste')
achar.search(string)
achar.findall(string)
achar.sub('abc', string)


