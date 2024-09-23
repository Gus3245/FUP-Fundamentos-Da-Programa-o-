matriz01 = []
matriz_n_d = []


def numero_primo(n1):
    if n1 == 0:
        return False
    if n1 == 2:
        return True

    for divisor in range(2, n1):
        if n1 % divisor == 0:
            return False

    return True


for linha1 in range(12):
    matriz01.append([])
    matriz_n_d.append([])
    for coluna in range(13):
        numero = int(input(""))
        matriz01[linha1].append(numero)

for coluna in range(13):
    maior_numero_primo = float("-inf")
    menor_numero = float("inf")
    for linha1 in range(12):
        if (
            numero_primo(abs(matriz01[linha1][coluna]))
            and matriz01[linha1][coluna] > maior_numero_primo
        ):
            maior_numero_primo = matriz01[linha1][coluna]
        if matriz01[linha1][coluna] < menor_numero:
            menor_numero = matriz01[linha1][coluna]

    if maior_numero_primo != float("-inf"):
        divisor = maior_numero_primo
    else:
        divisor = menor_numero

    for linha1 in range(12):
        matriz_n_d[linha1].append(matriz01[linha1][coluna] / divisor)

for item in matriz01:
    for numero in item:
        print(f"{numero:.2f}", end=" ")
    print()

print()

for item in matriz_n_d:
    for numero in item:
        print(f"{numero:.2f}", end=" ")
    print()
