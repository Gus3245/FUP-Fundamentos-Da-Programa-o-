num1 = float(input())
num2 = float(input())
num3 = float(input())
soma = 0



if(num1 >= num2):
    if(num1 >= num3):
        soma = num1
        print(f"{soma:.2f}")
        
if(num2 > num1):
    if(num2 > num3):
        soma = num2
        print(f"{soma:.2f}")
        
if(num3 > num1):
    if(num3 > num2):
        soma = num3
        print(f"{soma:.2f}")

