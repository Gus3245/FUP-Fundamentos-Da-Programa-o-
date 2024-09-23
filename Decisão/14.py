
while True:
    print('1 - Adicao')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')
    print('5 - Saida')

    escolhido=int(input())

    if escolhido==5:
        break

    numero_1=float(input())
    numero_2=float(input())
    
    if escolhido==1:
        soma=numero_1+numero_2
        print(f'{soma:.2f}')

    if escolhido==2:
        subtracao=numero_1-numero_2
        print(f'{subtracao:.2f}')

    if escolhido==3:
        multiplicacao=numero_1*numero_2
        print(f'{multiplicacao:.2f}')

    if escolhido==4:
        divisao=numero_1/numero_2
        print(f'{divisao:.2f}')
