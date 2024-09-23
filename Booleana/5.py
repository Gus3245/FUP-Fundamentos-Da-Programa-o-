cateto = int(input())
catOposto = int(input())
ipotenusa = int(input())

# Verificando se os lados estão de tamanhos corretos

if (cateto < (catOposto + ipotenusa) and catOposto < (cateto + ipotenusa) and (ipotenusa < (cateto + catOposto))):
    
    # equilatero
    if (cateto == catOposto) and (cateto == ipotenusa):
        print("Triangulo equilatero")
    
    # Escaleno
    elif(cateto != catOposto) and (cateto != ipotenusa) and (catOposto != ipotenusa):
        print("Triangulo escaleno")
    
    #isosceles
    else:
        print("Triangulo isosceles")


else:
    print("Não triangulo")
    
