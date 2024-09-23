from math import factorial

def funcao(x):
    n = 1
    for i in range(1 , x+1):
        n += 1 / factorial(i)
    
    return n
