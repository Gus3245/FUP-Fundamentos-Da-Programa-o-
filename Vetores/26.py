
def funcao(x1, x2):
    diferenca = []
    
    for valor in x1:
        
        if valor not in x2:
            if valor not in diferenca:
                diferenca.append(valor)
    
    return diferenca
