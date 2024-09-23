n_mais_novo = ""
i_mais_nova = None
n_mais_velho = ""
i_mais_velho = None   
while True:
    nome = str(input())
    idade = int(input())
    if idade < 0:
        break
    if i_mais_nova == None:
        i_mais_nova = idade
        n_mais_novo = nome
        i_mais_velho = idade
        n_mais_velho = nome
    else:
        if idade < i_mais_nova:
            i_mais_nova = idade
            n_mais_novo = nome
        if idade > i_mais_velho:
            i_mais_velho = idade
            n_mais_velho = nome
            
print(n_mais_novo)
print(i_mais_nova)
print(n_mais_velho)
print(i_mais_velho)
