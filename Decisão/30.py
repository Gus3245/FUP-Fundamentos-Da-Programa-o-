number1 = int(input())
contador = 0
conta_numeros = 1

while contador < number1:
    numeros = int(input())
    
    if contador == 0:
        highnumber = numeros
        
    
    elif(numeros > highnumber):
        highnumber = numeros
        conta_numeros = 1
        
    elif (numeros == highnumber):
        conta_numeros +=1
    contador += 1

print(highnumber)
print(conta_numeros)
