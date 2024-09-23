string = str(input())
Vogais = "aeiouAEIOU"
NewWord = string

for i in range(0, len(string)):
    for j in range(0, len(Vogais)):
        
        if(string[i] == Vogais[j]):
         NewWord =  NewWord.replace(string[i], "")
        

print(NewWord)


