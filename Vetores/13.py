import math

def funcao(x):
    soma = 0
    desviopadrao = 0
    count = 0
    
    for i in x:
        soma += i
        if (i < 7):
            count += 1
    
    soma = soma / len(x)
    desviopadrao = desvio(x, soma)
    
    return soma, desviopadrao, count
    
def desvio(x, soma):    
    _soma = 0
    
    for n in range(len(x)):
        _soma += (x[n] - soma) ** 2
        
    return math.sqrt(_soma / len(x))
    
