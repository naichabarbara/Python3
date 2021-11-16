'''
Um mágico escolheu um número secreto e escondeu-o numa variável chamada secret_number.
Ele quer que todos que joguem o jogo do adivinhe o número secreto, e adivinhe que número escolheu para eles.
Aqueles que não adivinharem o número ficarão presos num loop infinito para sempre

    Se o número for diferente do número secreto deve ter a mensagem "Ha ha! You're stuck in my loop!" 
    e ser solicitado a introduzir novamente um número;
    
    Se o número corresponder ao número escolhido pelo mágico, o número deve ser impresso no ecrã,
    e o mágico deve dizer as seguintes palavras: "Well done, muggle! You are free now."
'''

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input('Please, insert a number: '))

while number != secret_number:
    print('\nHa ha! You\'re stuck in my loop!')
    number = int(input('Reinsert a number: '))

print('The secret number is: {}!'.format(secret_number))
print('Well done, muggle! You are free now.')
