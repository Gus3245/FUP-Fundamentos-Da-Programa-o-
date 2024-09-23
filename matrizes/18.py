import random

aleatorio = int(input())
random.seed(aleatorio)

vetor = []
modificadvetor = []

for linha in range(5):
    vetor.append([])
    modificadvetor.append([])
    for coluna in range(5):
        numero = random.randint(1, 20)
        vetor[linha].append(numero)
        modificadvetor[linha].append([])


for linha in range(5):
    for coluna in range(5):
        modificadvetor[linha][coluna] = vetor[linha][coluna]


for linha in range(4):
    for number in range(1 + linha, 5):
        modificadvetor[linha][number] = 0


for linha in vetor:
    for number in linha:
        print(number, end=" ")
    print()

print()

for linha in modificadvetor:
    for number in linha:
        print(number, end=" ")
    print()
