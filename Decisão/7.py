salario = float(input())
prestacao = int(input())

if(prestacao > (salario / 5)):
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")
