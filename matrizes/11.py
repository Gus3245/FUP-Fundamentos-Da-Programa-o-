vetor = []
soma = 0

for linha in range(4):
    vetor.append([])
    for coluna in range(4):
        vetor[linha].append(int(input()))

for number in range(16):
    linha = number // 4
    coluna = number % 4
    if coluna + linha == 3:
        soma += vetor[linha][coluna]

print(soma)
