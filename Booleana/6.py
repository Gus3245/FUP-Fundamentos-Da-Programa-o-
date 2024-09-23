Age = int(input())
workTime = int(input())

if (Age < 65) and (workTime < 30):
    
    if(Age >= 60) and (workTime >= 25):
        print("Pode se aposentar")
    
    else:
        print("Nao pode se aposentar")


else:
    print("Pode se aposentar")


