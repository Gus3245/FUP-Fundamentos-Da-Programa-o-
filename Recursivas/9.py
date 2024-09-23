from math import factorial

def sf(x):
    if (x == 0) or (x == 1):
        return 1

    return factorial(x) * sf(x - 1)


