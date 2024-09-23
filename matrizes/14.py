vetor = []
secondvetor = []
thirdvetor = []
soma = 0

for linha in range(4):
    vetor.append([])
    thirdvetor.append([])
    for coluna in range(5):
        vetor[linha].append(int(input()))
        thirdvetor[linha].append([])

for linha in range(4):
    secondvetor.append([])
    for coluna in range(5):
        secondvetor[linha].append(int(input()))

for linha in range(4):
    for coluna in range(5):
        soma = vetor[linha][coluna] + secondvetor[linha][coluna]
        thirdvetor[linha][coluna] = soma
        soma = 0

for linha in thirdvetor:
    for number in linha:
        print(number, end=" ")

    print()
