contador = 0
num1 = int(input())

while contador != num1:
    numeros = float(input())
    if contador == 0:
        lownumber = numeros
        highnumber = numeros
        
    if (numeros > highnumber):
        highnumber = numeros
        
        
    if (numeros < lownumber):
        lownumber = numeros
    
    contador +=1

print(f"{lownumber:.2f}")
print(f"{highnumber:.2f}") 
