alunos = []

name = str(input("Aluno: "))
alunos.append(name)

while len(alunos) < 5:
    
    confirma = str(input("Deseja inserir novo aluno? [S/N] "))
    
    if confirma == "S":
        name = str(input("Aluno: "))
        alunos.append(name)
    
    elif confirma == "N":
        break

find = str(input("Aluno para pesquisa: "))

for i in range(len(alunos)):
    if find in alunos[i]:
        print(alunos[i])
        print(i)
