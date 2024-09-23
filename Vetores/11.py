list1 = []
soma = 0

for i in range(15):
    numero = float(input())
    list1.append(numero)

for i in range(15):
    soma += list1[i]

soma = soma / 15
print(f"{soma:.2f}")
