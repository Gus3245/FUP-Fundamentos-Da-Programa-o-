list1 = []
for i in range(8):
    numero = float(input())
    list1.append(numero)

x = int(input())
y = int(input())

soma = list1[x] + list1[y]
print(f"{soma:.2f}")

