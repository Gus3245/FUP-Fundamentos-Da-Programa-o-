soma = 0
multi = 1
cont = 2

while cont:
    number = int(input())
    if cont == 2:
        high = number
        low = number
        
    elif number > high:
        high = number
        
    elif number < low:
        low = number

    cont -=1

for i in range(low,high + 1):
    
    if(i % 2 == 0):
        soma += i
    
    else:
        multi *= i

print(soma)
print(multi)
