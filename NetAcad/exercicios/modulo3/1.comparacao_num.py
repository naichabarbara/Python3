'''
Faça um programa que compare três números diferentes e ao final apresente o maior valor entre eles.
Usar if-else e if-elif-else 
'''

# IF-ELSE
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))


largest_number = number1 #adimite o primeiro numero como maior para comparar aos outros

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("O maior valor é: ", largest_number)


# IF-ELIF-ELSE
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 > number2 and number1 > number3:
    largest_number = number1
elif number2 > number1 and number2 > number3:
    largest_number = number2
else:
    largest_number = number3

print("O maior valor é: ", largest_number)
