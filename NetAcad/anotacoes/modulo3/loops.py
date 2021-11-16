'''
O presente arquivo contém apenas comentários e trechos de códigos para apoio no aprendizado da linguagem Python!
'''

#Um loop pode ser representado da seguinte forma:
while {expressão condicional}:
    instrução
    
'''
Enquanto o IF executa a instrução apenas uma vez, o WHILE repete a execução enquanto a condição se avaliar
em True!

 --> While segue a mesma regra de identação. Suas instruções (ou conjunto delas) são chamadas de 'corpo do loop'
 --> A condição é testada ANTES de entrar no corpo do loop. Se false, as intruções não são executadas nem uma vez
  '''
  
#Execução 'KeyboardInterrupt' --> faz seu programa sair de um loop infinito

#EXEMPLO DE LOOPS
largest_number = -999999999

number = int(input("Enter a number or type -1 to stop: "))

while number != -1:
    if number > largest_number:
        largest_number = number

    number = int(input("Enter a number or type -1 to stop: "))

print("The largest number is:", largest_number)

#Pode ser utilizada a váriavel COUNTER (ou similar) para sair de um loop:
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# OU

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


'''
Pode usar aspas triplas para imprimir strings em várias linhas a fim de tornar o texto mais fácil de ler,
ou criar um desenho especial baseado em texto
'''

#LOOPS com for in range:
for i in range(100):
    # do_something()
    pass

'''
Qualquer palavra depois do 'for' é uma váriavel de controle
A função 'range()' é responsável por gerar todos os valores desejados dentro da váriavel de controle
                    - valores do 0 ao 99, no caso acima
                    
    OBS: é obrigatório conter pelo menos uma instrução dentro do for in range
'''

32.14