number = int(input())
contador = 0

for i in range(1, number + 1):
    if (number % i == 0):
        contador +=1
    
if(contador == 2):
    print("Primo")
else:
    print("Nao primo")
