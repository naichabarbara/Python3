'''
O presente arquivo contém apenas comentários e trechos de códigos para
apoio no aprendizado da linguagem Python!
'''

'''
Uma FUNÇÃO (no contexto da programação) é uma parte separada do código com função de:

 - Causar qualquer efeito - ex: criar arquivo, enviar mensagem ao terminal e entre outros;
  - Avaliar um valor e devolver como resultado de uma função.

      -- O nome de uma função deve ser significativo.

OBSERVAÇÃO: As funções exigem presença de um PAR DE PARÊNTESES - de abertura e fecho, mesmo sem argumentos.

Obrigatório o uso de aspas para DELIMITAR STRINGS na função, isso indica ao código a existencia de texto.
'''

print() #Imprime uma linha para o ecrã
#aceita qualquer tipo de argumentos mas NÃO ACEITA mais de uma instrução na mesma linha


'''
A barra invertida \ em uma string é um caractere de scape indicando que o próximo caractere será uma inclusão especial
    
   OBS: Por sua natureza de scape, tem de duplicar a barra invertida para invoca-lá no print - (sozinha)
'''

print("Hello, World! \nWelcome s2") #\n pula linha

'''
ARGUMENTOS DE KEYWORDS

Retira argumentos através da sua keyword (palavra-chave). Para utiliza-lá é necessário:
 - Consiste em três elementos: uma keyword, um sinal de igual e um valor atribuido ao argumento;
 - DEVE ser colocado após o último argumento posicional.
'''

print("Programming", "Essentials", "in", sep="**", end="-\n")
print("Python")
#sep --> separador de argumentos  /  end --> como o determinado print deve ser terminado
#só pode ser usado quando separado por VIRGULA no final do print para juntar a função com as strings

