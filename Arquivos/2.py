text_name = input()
with open(text_name, "r") as arquivo:
    quant = len(arquivo.readlines())

print(quant)
