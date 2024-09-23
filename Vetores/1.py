meses = (
    "janeiro",
    "fevereiro",
    "marco",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
)


def funcao(x):
    dia = int(x[0:2])
    mes = int(x[3:5])
    ano = int(x[6:])

    for i in range(len(meses)):
        if mes == 12:
            mes = meses[11]

        elif mes == i:
            mes = meses[i - 1]

    return f"{dia} de {mes} de {ano}"
