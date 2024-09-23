text_name = input()
quant = 0
with open(text_name, "r") as arquivo:
    for linha in arquivo:
        for palavra in linha:
            if palavra in "aeiou" or palavra in "AEIOU":
                quant += 1

print(quant)
