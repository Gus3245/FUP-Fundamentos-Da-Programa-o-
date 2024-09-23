vetor = []

for linha in range(4):
    vetor.append([])
    for coluna in range(4):
        vetor[linha].append(int(input()))

soma = 0
for linha in range(4):
    for coluna in range(4):
        if coluna < linha:
            soma += vetor[linha][coluna]

print(soma)
