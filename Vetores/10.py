list1 = []


for i in range(20):
    numero = int(input())
    list1.append(numero)

for i in range(20):
    if(list1[i] < 0):
        list1[i] = 0

for i in range(20):
    print(list1[i])
        
