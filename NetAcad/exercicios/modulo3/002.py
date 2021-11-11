'''
Calcule a taxa de imposto a partir das seguintes informações:
Rendimento do cidadão < 85.528 thalers, o imposto é igual a 18% - 556 thalers e 2 cêntimos;
Rendimento superior a esse valor, o imposto é igual a 14.839 thalers e 2 cêntimos + 32%.

Se o imposto calculado for <= 0 a taxa é zerada.
'''

income = float(input("Informe o rendimento atual: "))

if income <= 0:
    tax = 0
else:
    if income < 85528:
        tax = (income * 0.18) - 556.2
        if tax <= 0:
            tax = 0
    else:
        tax = (income * 0.32) + 14839.2


tax = round(tax, 0)
print("A taxa é:", tax, "thalers")
