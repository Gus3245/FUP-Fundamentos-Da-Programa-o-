
def funcao(x):
    length = len(x)
    
    for i in range(length):
        for j in range(length - i - 1):
            
            if x[j] < x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    
    return x
