vetor = []
secondvetor = []
matriz_produto = []

for linha in range(5):
    vetor.append([])
    for coluna in range(5):
        vetor[linha].append(int(input("")))

for linha in range(5):
    secondvetor.append([])
    for coluna in range(5):
        secondvetor[linha].append(int(input("")))

for item in range(5):
    matriz_produto.append([])
    for linha in range(5):
        soma = 0
        for coluna in range(5):
            soma += vetor[item][coluna] * secondvetor[coluna][linha]
        matriz_produto[item].append(soma)

for item in matriz_produto:
    for numero in item:
        print(numero, end=" ")
    print()
