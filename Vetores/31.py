text = str(input())
compare = []

for letter in text:
    if letter.isalpha():
        if letter not in compare:
            compare.append(letter)

count = len(compare)
print(count)
