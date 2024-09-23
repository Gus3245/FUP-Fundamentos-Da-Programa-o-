
def funcao(x1, x2):
    intersec = []

    
    for valor in x1:
        for i in range(5):
            
            if(valor == x2[i]):
                intersec.append(valor)
                break
        
    
    intersec = list(set(intersec))
    
    return intersec
