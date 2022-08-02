# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

numero_verificado = int(input())
inicio = [0, 1]
sequencia_fibonacci = []
limite = 10000

def fibonacci():
    for i in range(limite):
        if(i == 0 or i == 1):
            sequencia_fibonacci.append(inicio[i])
        else:
            sequencia_fibonacci.append(sequencia_fibonacci[i-1] + sequencia_fibonacci[i-2])


def verificacao():
    if numero_verificado in sequencia_fibonacci:
        print("Este número pertence à sequência de Fibonacci")
    else:
        print("Este número não pertence à sequência de Fibonacci")

fibonacci()
verificacao()
