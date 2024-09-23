vetor = []
percorrer = 1

while (len(vetor)) < 100:
    if(percorrer % 7 != 0) and(percorrer % 10 != 7):
        vetor.append(percorrer)
    
    percorrer += 1

print(vetor)
