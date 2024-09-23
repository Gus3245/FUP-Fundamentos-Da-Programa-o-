with open("arq.txt", "a") as arquivo:
    while True:
        linha = input()

        if linha == "0":
            break
        arquivo.write(linha + "\n")
arquivo.close

with open("arq.txt", "r") as arquivo:
    texto = arquivo.read()

print(texto)
