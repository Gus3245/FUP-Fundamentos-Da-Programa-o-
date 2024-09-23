from math import factorial

def funcao(P):
    fatoracao = factorial(P)
    soma = 0
    while fatoracao:
        soma += fatoracao % 10
        fatoracao //= 10
          
    return soma



