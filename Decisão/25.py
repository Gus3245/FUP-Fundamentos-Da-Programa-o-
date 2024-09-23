contador=0
contador_negativos=0
resultado=0

while contador!=10:
    numeros=int(input())
    
    if numeros>0:
        contador+=1
        resultado+=numeros
    media=(resultado)/(10)

print(f'{media:.2f}')
