def funcao(x):
    for i in range(1, x+1):
        print(" " * (x-1), end="")
        x = x-1
        print("*" * (2* i-1))
       
