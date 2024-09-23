list1 = []
count = 0

for i in range(15):
    numero = int(input())
    list1.append(numero)

for i in range(15):
    if (list1[i] % 2 == 0):
        count = count + 1

print(count)
for i in range(15):
    if (list1[i] % 2 == 0):
        print(list1[i])
