length = int(input())
vetor = []

for linha in range(length):
    vetor.append([])
    for coluna in range(length):
        vetor[linha].append(0)

for i in range(length):
    vetor[i][i] = 1

for item in vetor:
    for coluna in item:
        print(coluna, end=" ")

    print()
