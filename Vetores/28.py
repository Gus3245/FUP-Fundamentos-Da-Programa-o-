numbers = 0
vetornumbers = []

    
while numbers < 12:
    number = int(input())
    
    if number not in vetornumbers:
        vetornumbers.append(number)
        numbers += 1
        
    else:
        print(f"Numero {number} ja existe, escreva outro")

print(vetornumbers)
