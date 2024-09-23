vetor = []
modificadevetor = []

for linha in range(12):
    vetor.append([])
    modificadevetor.append([])
    for coluna in range(13):
        vetor[linha].append(int(input()))
        modificadevetor[linha].append([])


for linha in range(12):
    highnumber = 0

    for number in range(13):
        if highnumber < abs(vetor[linha][number]):
            highnumber = abs(vetor[linha][number])

    for item in range(13):
        modificadevetor[linha][item] = vetor[linha][item] / highnumber


for linha in vetor:
    for number in linha:
        print(f"{number:.2f}", end=" ")
    print()

print()

for linha in modificadevetor:
    for number in linha:
        print(f"{number:.2f}", end=" ")
    print()
