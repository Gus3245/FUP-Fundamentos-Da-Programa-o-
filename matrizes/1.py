vetor = []
count = 0

for linha in range(4):
    vetor.append([])
    for coluna in range(4):
        vetor[linha].append(int(input()))

for i in range(4):
    for j in range(4):
        if vetor[i][j] > 10:
            count += 1

print(count)
