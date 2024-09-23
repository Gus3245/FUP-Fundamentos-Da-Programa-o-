num1 = int(input())
total = 0

for i in range(1, 100):
    if (i != num1):
        if (num1 % i == 0):
            total += i
            
print(total)
