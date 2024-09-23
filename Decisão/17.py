num1 = 1
quadrado = 0
cubo = 0
raiz = 0

while num1 > 0:

    num1 = int(input())

    if( num1 <= 0 ):
        break

    quadrado = num1 ** 2
    cubo = num1 ** 3
    raiz = num1 ** (1/2)

    print(f"{quadrado:.2f}")
    print(f"{cubo:.2f}")
    print(f"{raiz:.2f}")
