zeros_e_uns = str(input())
zero = '0'
um = '1'
len_zero = len(zero)
nova_string = ""

i = 0
while i < len(zeros_e_uns):
    if zeros_e_uns[i:i + len_zero] == zero:
        nova_string += um
        i += len_zero
    else:
        nova_string += zeros_e_uns[i]
        i += 1
print(nova_string)
