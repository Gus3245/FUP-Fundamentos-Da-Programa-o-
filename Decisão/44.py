frase = str(input())
f_invertida = ''
for i in range(len(frase) -1,-1,-1):
    letra = frase[i]
    if letra == 'A':
        f_invertida += '*'
    elif letra == 'a':
        f_invertida += '*'
    else:
        f_invertida += letra
print(f_invertida)
