A = []

for linha in range(10):
    A.append([])
    for coluna in range(10):
        A[linha].append(0)

for i in range(10):
    for j in range(10):
        if i < j:
            A[i][j] = 2 * i + 7 * j - 2

        elif i > j:
            A[i][j] = 4 * (i**3) - 5 * (j**2) + 1

        else:
            A[i][j] = 3 * i**2 - 1

for i in range(10):
    for j in range(10):
        print(A[i][j], end=" ")

    print()
