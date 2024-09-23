bissexto = int(input())

if (bissexto % 4 == 0) and (bissexto % 100 != 0):
    print("Bissexto")

elif (bissexto % 400 == 0):
    print("bissexto")

else:
    print("Nao bissexto")
