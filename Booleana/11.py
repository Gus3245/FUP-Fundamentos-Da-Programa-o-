

def funcao(x):
    divisoria = x.split("/")

    if len(divisoria) != 3:
        return 0,0,0
    y1,y2,y3 = divisoria

    if not (1 <= len(y1) <= 2 and 1 <= len(y2) <= 2 and 1 <= len(y3) <= 4):
        return 0, 0, 0
    
    for i in divisoria:
        if not i.isdigit():
            return 0, 0, 0

    y1 = int(y1)
    y2 = int(y2)
    y3 = int(y3)
    if (y1 > 0 and y1 < 32) and (y2 > 0 and y2 <= 12) and (y3 > 0 and y3 <= 9999):
        return y1, y2, y3
    else:
        return 0, 0, 0
