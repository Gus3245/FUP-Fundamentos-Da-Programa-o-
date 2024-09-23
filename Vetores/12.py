import math

def funcao(x):
    soma = 0
    desviopadrao = 0
    
    for i in x:
        soma += i
    
    soma = soma / len(x)
    desviopadrao = desvio(x, soma)
    
    return soma, desviopadrao
    
def desvio(x, soma):    
    _soma = 0
    
    for n in range(len(x)):
        _soma += (x[n] - soma) ** 2
        
    return math.sqrt(_soma / len(x))
    

