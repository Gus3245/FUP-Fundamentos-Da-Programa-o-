vetor = []

for i in range(10):
    vetor.append(int(input()))
    
for item in range(10):
    for valor in range(item + 1, 10):
        if vetor[item] == vetor[valor]:
            print(vetor[item])

