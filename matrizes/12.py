vetor = []
secondvetor = []

for linha in range(4):
    vetor.append([])
    secondvetor.append([])
    for coluna in range(4):
        vetor[linha].append(int(input()))

for linha in range(4):
    for coluna in range(4):
        secondvetor[coluna].append(vetor[linha][coluna])

for item in secondvetor:
    for number in item:
        print(number, end=" ")
    print()
