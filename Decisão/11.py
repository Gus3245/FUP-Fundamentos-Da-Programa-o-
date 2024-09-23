num1 = float(input())
operand = input()
num2 = float(input())

if operand == "+":
    total = (num1 + num2)
    print(f"{total:.2f}")
    
if operand == "-":
    total = (num1 - num2)
    print(f"{total:.2f}")
    
if operand == "/":
    total = (num1 / num2)
    print(f"{total:.2f}")

if operand == "*":
    total = (num1 * num2)
    print(f"{total:.2f}")
