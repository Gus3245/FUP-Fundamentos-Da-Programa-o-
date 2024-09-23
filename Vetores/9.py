list1 = []
lownumber = 100
highnumber = 0

for i in range(10):
    numero = int(input())
    list1.append(numero)

for i in range(10):
    
    if(lownumber > list1[i]):
        lownumber = list1[i]
    
    if(highnumber < list1[i]):
        highnumber = list1[i]

print(highnumber)
print(lownumber)
