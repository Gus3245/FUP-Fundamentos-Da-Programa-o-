def funcao(lista):
    tl = len(lista)
    if tl < 2:
        return -1, -1, -1
    
    tm = 0
    c1 = -1
    c2 = -1
    for ts in range(2, tl):
        for item in range(tl - ts + 1):
            s1 = lista[item:item+ts]
            
            for posicao_comparacao in range(item + 1, tl - ts + 1):
                s2 = lista[posicao_comparacao:posicao_comparacao + ts]
                
                if s1 == s2 and ts > tm:
                    tm = ts
                    c1 = item
                    c2 = posicao_comparacao
                    break
                    
    if tm == 0:
        return -1, -1, -1
    else:
        return c1, c2, tm
