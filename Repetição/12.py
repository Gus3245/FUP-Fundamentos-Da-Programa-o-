from math import factorial

def funcao(x1, x2):
    for i in range(10):
        i = factorial(x1) / (factorial(x2) * factorial((x1-x2)))
        
    return i
