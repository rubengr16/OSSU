# Given a number through input, it converts it to decimal
bin_num = input('Enter a binary number to convert to hexadecimal: ')
print(bin_num, 'in hexadecimal is', end=' ')
resul = ''
bin_num_intgr = str(int(float(bin_num) // 1))
bin_num_flt = bin_num[len(bin_num_intgr) + 1:]


for i in range(2):  # 2 iterations: 0 for decimal part, 1 for fractional one
    if i == 0:
        aux = bin_num_intgr
    else:
        aux = bin_num_flt

    while len(aux) > 0:
        if len(aux) > 4:  # In the case we have enough digits
            act = aux[len(aux) - 4:]
            aux = aux[:len(aux) - 4]
        else:  # If we don't have enough, we add 0s to the right
            if i == 0:  # In decimal part, not significant 0s are added on the right
                act = '0' * (4 - len(aux)) + aux
            else:  # In fractional, they are added on the left
                act = aux + '0' * (4 - len(aux))
            aux = ''
        n = None
        # Creation of a switch for each of the 16 possible hexadecimal numbers
        if act == '0000':
            n = '0'
        elif act == '0001':
            n = '1'
        elif act == '0010':
            n = '2'
        elif act == '0011':
            n = '3'
        elif act == '0100':
            n = '4'
        elif act == '0101':
            n = '5'
        elif act == '0110':
            n = '6'
        elif act == '0111':
            n = '7'
        elif act == '1000':
            n = '8'
        elif act == '1001':
            n = '9'
        elif act == '1010':
            n = 'A'
        elif act == '1011':
            n = 'B'
        elif act == '1100':
            n = 'C'
        elif act == '1101':
            n = 'D'
        elif act == '1110':
            n = 'E'
        elif act == '1111':
            n = 'F'

        if i == 0:
            resul = n + resul
        else:
            resul += n
    if i == 0:
        resul += '.'

print(resul)
