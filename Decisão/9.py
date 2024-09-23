numero_1=int(input())
numero_2=int(input())
numero_3=int(input())

#3 digito sendo o maior
if numero_1<numero_2:
    if numero_1<numero_3:
        if numero_2<numero_3:
            print(numero_1)
            print(numero_2)
            print(numero_3)

if numero_1<numero_3:
    if numero_1>numero_2:
        if numero_2<numero_3:
            print(numero_2)
            print(numero_1)
            print(numero_3)

if numero_1==numero_2:
    if numero_1<numero_3:
        print(numero_1)
        print(numero_2)
        print(numero_3)

#2 digito sendo o maior
if numero_1<numero_2:
    if numero_1<numero_3:
        if numero_3<numero_2:
            print(numero_1)
            print(numero_3)
            print(numero_2)

if numero_1>numero_3:
    if numero_1<numero_2:
        if numero_2>numero_3:
            print(numero_3)
            print(numero_1)
            print(numero_2)

if numero_1==numero_3:
    if numero_2>numero_1:
        print(numero_1)
        print(numero_3)
        print(numero_2)


#1 sendo o maior
if numero_1>numero_2:
    if numero_1>numero_3:
        if numero_2>numero_3:
            print(numero_3)
            print(numero_2)
            print(numero_1)

if numero_1>numero_2:
    if numero_1>numero_3:
        if numero_2<numero_3:
            print(numero_2)
            print(numero_3)
            print(numero_1)

if numero_2==numero_3:
    if numero_2<numero_1:
        print(numero_2)
        print(numero_3)
        print(numero_1)


#situações de igualdade
if numero_3==numero_1==numero_2:
    print(numero_1)
    print(numero_2)
    print(numero_3)

if numero_2==numero_3:
    if numero_2>numero_1:
        print(numero_1)
        print(numero_2)
        print(numero_3)

if numero_1==numero_2:
    if numero_3<numero_1:
        print(numero_3)
        print(numero_2)
        print(numero_1)

if numero_1==numero_3:
    if numero_3>numero_2:
        print(numero_2)
        print(numero_3)
        print(numero_1)
