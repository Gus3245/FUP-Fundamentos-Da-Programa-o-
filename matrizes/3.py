length = int(input())
vetor = []

for linha in range(length):
    vetor.append([])
    for coluna in range(length):
        vetor[linha].append(linha * coluna)


for item in vetor:
    for number in item:
        print(number, end=' ')

    print()
    
