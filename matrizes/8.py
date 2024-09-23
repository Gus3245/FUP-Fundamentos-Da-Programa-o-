vetor = []

for linha in range(4):
    vetor.append([])
    for coluna in range(4):
        vetor[linha].append(int(input()))

soma = 0
for i in range(4):
    for j in range(i + 1, 4):
        soma += vetor[i][j]

print(soma)
