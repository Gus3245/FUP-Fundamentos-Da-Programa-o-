vetor = []

for i in range(10):
    number = int(input())
    vetor.append(number)
    
for posi, num in enumerate(vetor):
    v = 0
    number = abs(num)
    
    for j in range(1, number + 1):
        if number % j == 0:
            v += 1
    
    if v == 2:
        print(num)
        print(posi)
