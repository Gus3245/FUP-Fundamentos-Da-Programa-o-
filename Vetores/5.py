list1 = []
double = []

for i in range(10):
    numero = float(input())
    list1.append(f"{numero:.2f}")
    print(f"{list1[i]}")
    
for valor in list1:
    double.append(float(valor))
    

for i in range(10):
    double[i] = double[i] ** 2
    print(f"{double[i]:.2f}")
