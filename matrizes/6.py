vetor = []
secondvetor = []
thirdvetor = []


for linha in range(4):
    vetor.append([])
    thirdvetor.append([])
    for coluna in range(4):
        vetor[linha].append(int(input()))
        thirdvetor[linha].append([])

for linha in range(4):
    secondvetor.append([])
    for coluna in range(4):
        secondvetor[linha].append(int(input()))


for i in range(4):
    for j in range(4):
        if vetor[i][j] > secondvetor[i][j]:
            thirdvetor[i][j] = vetor[i][j]

        elif secondvetor[i][j] >= vetor[i][j]:
            thirdvetor[i][j] = secondvetor[i][j]

for linha in range(4):
    for numero in range(4):
        print(thirdvetor[linha][numero], end=" ")

    print()
