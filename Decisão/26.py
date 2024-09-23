contador = 0
highnumber = 0
lownumber = 100

while contador != 10:
    numeros = int(input())
    
    if (numeros > 0):
        
        if (numeros > highnumber):
            highnumber = numeros
        
        
    if (numeros <= lownumber):
        lownumber = numeros
    
    contador +=1

print(f"{lownumber:.2f}")
print(f"{highnumber:.2f}") 


