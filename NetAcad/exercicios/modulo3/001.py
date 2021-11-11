'''
Programa que identific um ano bissexto ou ano comum:
    Anos bissextos fazem parte do calendário Gregoriano que foi criado a partir de 1582. Esses anos são 
    divisíveis por 4.
'''

year = int(input("Enter a year: "))

if year <= 1581:
    print('Não faz parte do perído de criação do Calendário Gregoriano!')
else:
    if year % 4 != 0:
        print('O ano {} é um ano comum!'.format(year))
    else:
        print('O ano {} é um ano bissexto!'.format(year))
        