
def funcao(x1, x2):
    multiplos = []
    
    for valor in x1:
        number = valor
        if(number % x2 == 0):
            multiplos.append(number)

    return multiplos
