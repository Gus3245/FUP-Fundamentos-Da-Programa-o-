    

string = str(input())
caracter = str(input())
NewWord = string
Acumulador = 0
Vogais = "aeiouAEIOU"


for i in range(0, len(string)):
    for vogal in Vogais:
        
        if (string[i] == vogal):
            NewWord = NewWord.replace(string[i], caracter)
            Acumulador += 1

print(Acumulador)
print(NewWord)


