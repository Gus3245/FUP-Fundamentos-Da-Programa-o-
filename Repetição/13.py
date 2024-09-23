def funcao(x):
    f1 = 1
    f2 = 1
    f3 = 1
    
    for i in range(1 , x-1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    
    return f3
    
