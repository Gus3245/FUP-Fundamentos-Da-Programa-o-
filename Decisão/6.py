media = 0
nota_invalida = True

for i in range(3):
    notas = float(input())

    if notas < 0:
        print("Nota invalida")
        nota_invalida = False
        break

    elif notas > 10:
        print("Nota invalida")
        nota_invalida = False
        break

    media += notas

if nota_invalida:
    media = media / 3
    print(f"{media:.2f}")

