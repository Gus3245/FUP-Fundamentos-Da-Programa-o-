
def funcao(x):
    if (x == 0):
        print(0)

    else:
        funcao(x - 1)
        if( x % 2 == 0):
            print(x)
