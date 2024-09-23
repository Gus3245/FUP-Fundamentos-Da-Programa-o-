vetor = []
secondvetor = []
soma = 0

for linha in range(5):
    vetor.append([])
    secondvetor.append([])
    for coluna in range(5):
        vetor[linha].append(int(input()))

for linha in range(5):
    for coluna in range(5):
        soma += vetor[coluna][linha]

    secondvetor[linha] = soma
    soma = 0

print(secondvetor)
