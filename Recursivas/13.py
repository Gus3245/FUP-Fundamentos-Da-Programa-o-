
def A(x1, x2):

    if (x1 == 0):
        return x2 + 1

    if (x1 > 0) and (x2 == 0):
        return A(x1 - 1, 1)
    
    elif (x1 > 0) and (x2 > 0):
        return A(x1 - 1, A(x1, x2 - 1))
