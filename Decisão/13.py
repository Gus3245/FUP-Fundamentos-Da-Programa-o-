a = float(input())
b = float(input())
c = float(input())

delta= b ** 2+(-4 * a * c)
if a==0:
    print('Nao eh equacao do 2o grau')

if a!=0:
    if delta > 0:
        x1 = (-b +delta ** (1/2)) / (2 * a)
        x2 = (-b -delta ** (1/2)) / (2 * a)
        print(f'{x1:.2f}')
        print(f'{x2:.2f}')
            

if delta < 0:
    print('Nao existe raiz real')

if a!=0:
    if delta==0:
        x1 = (-b +delta ** (1/2)) / (2 * a)
        print(f'{x1:.2f}\nRaiz unica ')
