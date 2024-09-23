import random

aleatorio = int(input())
random.seed(aleatorio)

vetor = []
positivos = 0
negativos = 0
soma = 0

for i in range(12):
    number = random.uniform(-10, 10)
    vetor.append(number)


for valor in vetor:
    if valor <= 0:
        negativos += 1

    else:
        soma = soma + valor
        positivos += 1

print(negativos)
print(f"{soma:.2f}")
