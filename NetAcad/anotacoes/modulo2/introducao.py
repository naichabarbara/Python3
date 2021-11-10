'''
O presente arquivo contém apenas comentários e trechos de códigos para
apoio no aprendizado da linguagem Python!
'''

#Pode se dizer que PCs executam um conjunto de comandos pré-determinados e conhecidos (programas)
#Um conjunto de tarefas (ações) formam um programa de computador

#conjunto completo de comandos formam uma Lista de Instruções (Instruction List) - alfabeto da máquina

'''
Cada linguagem precisa de 4 elementos para ser completa:

1. Um alfabeto com um conjunto de símbolos para construir palavras;
2. Um lexis (dicionário);
3. Uma sintaxe que é o conjunto de regras para validar uma palavra;
4. Uma semântica que verifica se uma frase/palavra tem sentido,
'''

#PROGRAMAÇÃO DE ALTO NÍVEL: Linguagem mais próxima da linguagem humana;
#PROGRAMAÇÃO DE BAIXO NÍVEL: Linguagem mais próxima da linguagem de computadores.

#programa escrito em linguagem de alto nível é chamado de SOURCE CODE, encontrado no ficheiro SOURCE FILE

'''
COMPILAÇÃO X INTERPRETAÇÃO

Compilação: Um programa é traduzido para a linguagem de máquina uma vez (caso não tenha alterações no código) e salva essa tradução em um arquivo executável;

Interpretação: Traduz a linguagem a cada vez que o arquivo é executado - executa diretamente cada comando.

O interprete verifica se todos os critério de linguagem (alfabeto, lexis, sintaxe e semântica) estão corretos e logo após executa o programa linha por linha
'''

'''
VANTAGENS E DESVANTAGENS 

Compilação -->
    Vantagens: execução mais rápida (por estar traduzido); o end-user não precisa ter o compilador; armazenado em linguagem de máquina (seguro).
    Desvantagens: pode não executar rápido durante alterações (compilar demora).
    
Interpretação --> 
    Vantagens: não a fase adicional de tradução (entre alterações); executável em qualquer PC que utiliza código de máquina diferente (armazenado em linguagem de máquina). 
    Desvantagens: um pouco mais demorado; o end-user também tem que ter o interprete. 
'''

#Python é uma linguagem interpretada, orientada a objetos e Open Source - linguagem de scripting (concebida para ser usada com interpretação)

#OBSERVAÇÃO: Scripts do Python 2 não vão rodar no Python 3 por terem algumas incompatibilidades

'''
CPYTHON

Existem outros Pythons - mantidos pelo o PSF (Python Software Fundation) - que são chamados de canónicos. Todos seguem normas estabelecidas pela a fundação - escritos em linguagem C

        -- Por esse motivo, a implantação da PSF é chamado de CPython
        -- Implementação padrão da linguagem Python
'''

#Para saber a versão do Python -- $python
#ferramenta 'debugger' que faz a inspeção do código


