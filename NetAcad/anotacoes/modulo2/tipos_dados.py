'''
O presente arquivo contém apenas comentários e trechos de códigos para apoio no aprendizado da linguagem Python!
'''

'''
Tipos primitivos:
STR = cadeia de caracteres e strings
INT = números positivos, negativos e nulo (0) - podem ser usados undercores _ para separar as casas
FLOAT = números reais (com ponto) positivos e negativos
        --> Pode usar a letra e para fazer separação dos decimais, como por exemplo: transformar o numero 3x10^8 em 3e8 - abreviações
        - e vem da palara 'exponeciação' e registra a frase 'vezes 10 elevado a potencia de.."
        - o valor depois do e DEVE ser um inteiro
BOOL = apresenta um valor truthfulness (veracidade) -- verdadeiro ou falso (True or False - com letra maiúscula)

Função "type" para saber o tipo da variável
'''

print(0o123) #se o número for precedido por 0o ele será tratado como um valor octal (sistema base 8)
print(0x123) #0x para tratar de numeros hexadecimais (sistema base 16)

print(0.0000000000000000000001) #mostra 1e-22
#tem esse resultado pelo o Python sempre apresentar os números de forma mais economica

print("I like \"Monty Python\"") #usa barra invertida para delimitar aspas dentro de aspas
print('I like "Monty Python"') #outro jeito de delimitar aspas é começar a string por apóstrofes
print() #Uma string vazia, ainda assim é uma string

print(int("1011", 2)) #converte o número binário para decimal (trocar o valor da base para converter outros tipos)

'''
Operadores básicos (em ordem de prioridade):

+  --  capaz de somar os números
-  --  capaz de subtrair os números
** --  reseprenta exponenciação - argumento esquerdo como base e direito como expoente
*  --  capaz de multiplicar os números
/  --  capaz de dividir os números - com resultado float
// --  capaz de dividir os números - com resultado inteiro arredondados para o menor -- floor division
%  --  apresenta o resto de uma divisão


    PYTHON SEGUE HIERARQUIA DE PROPRIEDADES NA RESOLUÇÃO DE CÁLCULOS
    
    Exponenciação utiliza ligação de operadores do lado direito para o esquerdo
'''

#Operador binário necessita de dois operandos para se chegar a um resultado

pow(4,3) #corresponde a 4 elevado a 3

c = (a ** 2 + b ** 2) ** 0.5 #** 0.5 avalia como raiz quadrada
x = x * 2
x *= 2 #maneira abreviada da expressão acima


#Converter kilometros em milhas e vice-versa
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")  #função 'round' arredonda números
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#representar a multiplicação (3x³ - 2x² + 3x - 1) atribuindo o valor a Y
x = -1
x = float(x)
y = ((3 *(x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1)
print("y =", y)


