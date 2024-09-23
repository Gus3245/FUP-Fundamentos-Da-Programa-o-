
def funcao(x):
    if (x == 1) or (x == 2):
        return x
    
    return 2*funcao(x - 1) + 3*funcao(x - 2)

    

