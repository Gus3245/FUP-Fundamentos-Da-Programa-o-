word = str(input())
count = 0

for i in range(len(word)):
    if( word[i] == " "):
        count += 1
        
print(count)
