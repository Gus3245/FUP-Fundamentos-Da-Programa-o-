number1 = float(input())
number2 = float(input())
operation = int(input())

result = 0

if operation == 1:
    result = (number1 + number2) / 2
elif operation == 2:
    if (number1 > number2):
        result = number1 - number2
    elif (number2 > number1):
        result = number2 - number1
    else:
        result = 0

elif operation == 3:
    result = number1 * number2

elif operation ==  4:
    if number1 == 0:
        result = 0
    elif number2 == 0:
        result = "Erro"
    else:
       result = number1 / number2

else:
    result = "Erro"

if result == "Erro":
    print(result)
else:
    print(f"{result:.2f}")
