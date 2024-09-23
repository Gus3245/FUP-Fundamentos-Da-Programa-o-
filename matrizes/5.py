vetor = []
for linha in range(5):
    vetor.append([])
    for coluna in range(5):
        vetor[linha].append(int(input()))

x = int(input())
incidencia = False
found = 0

for linha in vetor:
    for numero in linha:
        if numero == x:
            incidencia = True


if not incidencia:
    print("Nao encontrado")

for posilinha, item in enumerate(vetor):
    for posicoluna, numero in enumerate(item):
        if numero == x and incidencia:
            print(posilinha)
            print(posicoluna)
            incidencia = False
        break
