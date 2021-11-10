'''
O presente arquivo contém apenas comentários e trechos de códigos para apoio no aprendizado da linguagem Python!
'''

#O comando 'input()' tem a função de ler dados digitados pelo o usuário e retornar o dado em uma execução do programa
#programas que não recem input do usuário, são programas surdos

#Dados de Input devem ser armazenados em uma variável para não se perder, da seguinte maneira:
nome = input("Escreva seu nome: ")

#Todos os resultados da função input() serão uma string a menos que seja declarado o seu tipo antes:
numero = int(input("Digite um número inteiro: "))

'''
EXEMPLO DE CÓDIGOS

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

Ou mais simplificado:

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)
'''

#Sinal de + pode servir como um concatenador de duas STRINGS
fname = input("Digite seu primeiro nome: ")
lname = input("Digite seu último nome: ")
print("Seu nome é: " + fname + " " + lname + " ")

#Sinal de * tem a função de replicar uma string quando aplicado em uma string + numero:
print("James" * 3)  #resultado igual a "JamesJamesJames"

#Desenhando um retângulo usando os operadores de outra maneira:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#A função str() converte números em STRINGS
str(2) 


# Junção de tudo visto até agora: print("A soma de " + str(a_value) + " + " + str(b_value) + " é = ", round(a_value + b_value, 3))

'''
Duração de um evento (não consegui concluir)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')
'''

print(type(x)) #para verificar o tipo do dado X