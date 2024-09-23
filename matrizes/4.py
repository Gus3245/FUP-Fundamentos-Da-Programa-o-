vetor = []
highnumber = 0
contador = 0
incidencia = True

for linha in range(4):
    vetor.append([])
    
for linha in vetor:
    for i in range(4):
        linha.append(int(input()))
        
        
for linha in vetor:
    for numero in linha:
        
        if contador == 0:
            highnumber = numero
        else:
            if numero > highnumber:
                highnumber = numero
                
        contador += 1
        
for item in vetor:
    for number in item:
        print(number, end=' ')

    print()
    
for posilinha, item in enumerate(vetor):
    for posicoluna, numero in enumerate(item):
        if highnumber == numero and incidencia:
            print(posilinha)
            print(posicoluna)
            print(highnumber)
            incidencia = False
            
