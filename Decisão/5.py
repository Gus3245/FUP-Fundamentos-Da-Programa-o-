from math import sqrt

number1 = float(input())
square = 0

if (number1 > 0):
    square = sqrt(number1)
    print(f" {square:.2f} ")
else:
    print("Numero invalido")
