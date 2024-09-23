vetor = []
soma = 0

for linha in range(4):
    vetor.append([])
    for coluna in range(4):
        vetor[linha].append(int(input()))


for number in range(4):
    soma += vetor[number][number]

print(soma)
