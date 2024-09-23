
def funcao(x1, x2):
    uniaovetor = []
    
    
    for i in x1:
        if i not in uniaovetor:
            uniaovetor.append(i)
    for i in x2:
        if i not in uniaovetor:
            uniaovetor.append(i)
            
    return uniaovetor
