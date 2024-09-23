vetor = []
contine = True
invertevetor = []

for i in range(100):
    vetor.append(float(input()))

while contine == True:
    
    code = int(input())
    
    if code == 0:
        contine = False
        break
    
    elif code == 1:
        
        for i in range(100):
            print(vetor[i])
            
    
    elif code == 2:
        
        for i in range(len(vetor) -1,-1,-1):
            invertevetor.append(vetor[i])
        
        for i in range(100):
            print(invertevetor[i])
    
    else:
        print("Codigo invalido")
