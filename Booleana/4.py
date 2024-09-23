number = int(input())

if(number % 3 == 0 and number % 5 == 0):
    print("False")
elif(number % 3 == 0 or number % 5 == 0):
    print("True")
else:
    print("False")
