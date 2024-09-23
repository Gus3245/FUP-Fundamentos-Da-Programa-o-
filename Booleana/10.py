def funcao(x1, x2):
    while x2 != 0:
        resto = x1 % x2
        x1 = x2
        x2 = resto

    return x1
