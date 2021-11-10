'''
O presente arquivo contém apenas comentários e trechos de códigos para apoio no aprendizado da linguagem Python!
'''

# == operador binário para comparar igualdade - usado com apenas 2 argumentos
# != operador que compara desigualdade entre dois argumentos

black_sheep == (2 * white_sheep) #faz o dobro da contagem de ovelhas brancas comparado a ovelhas pretas

# > (maior que) compara se um número é MAIOR que outro
# < (menor que) compara se um número é MENOR que outro
        # variações especiais >= (maior ou igual)  /   <= (menor ou igual)
        
   
#Usa-se EXECUÇÃO CONDICIONAL para quando é preciso realizar uma instrução se a condição for verdadeira (ou falsa)

'''
Declaração condicional (IF) segue a seguinte estrutura:

 - Keyword "if' com um espaço em branco seguido do argumento (comparativo) e dois pontos
 - Newline com a instrução identada (por TAB)
 
 if true_or_not:
    do_this_if_true
    
OBS: Não é premitido espaços + TABs para fazer a identação do código
'''

#Estrutura (IF-ELSE) segue a mesma do exemplo anterior, com a complementação do ELSE:
if true_or_not:
        do_this_if_true
else:                            #Cada ELSE refere-se a um IF
        do_not_do_if_false
        


'''
DECLARAÇÃO ELIF:

Usado para verificar mais de uma condição e para quando a primeira afirmação verdadeira for encontrada.
Segue a mesma estrutura do if (que vem argumentos a sua frente):

if the_weather_is_god:
        go_for_a_walk()
elif tickets_are_available:
        go_to_the_theater()
else:
        play_chess_at_home()
        
        
DECLARAÇÕES IF-ELIF-ELSE SÃO CHAMADAS DE 'CASCATA' (CASCADE)
'''

#Se houver ELSE na cascata, APENAS UM de todos os ramos É EXECUTADO
#Se não houver ELSE na cascata, pode ser que NENHUM RAMO seja EXECUTADO

#Se algum dos ramos (IF-ELIF-ELSE) conter apenas UMA instrução, pode colocar a instrução na mesma linha que a condição (não recomendado):
if number_1 > number_2: larger_number = number_1
else: larger_number = number_2


#Pode ser usada a função max() para retornar o maior valor em meio a multiplos argumentos
largest_number = max(number_1, number_2, number_3)
#Já a função min() retorna o menor valor