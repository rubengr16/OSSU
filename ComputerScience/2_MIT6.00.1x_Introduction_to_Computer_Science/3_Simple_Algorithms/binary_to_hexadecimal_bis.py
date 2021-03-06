# Given an integer through input, it converts it to decimal
bin_num = input('Enter a binary integer to convert to hexadecimal: ')
print(bin_num, 'in hexadecimal is', end=' ')
is_neg = None
resul = ''

if bin_num[0] == '-':
    is_neg = True
    bin_num = bin_num[1:]
else:
    is_neg = False

while len(bin_num) > 0:
    if len(bin_num) > 4:
        act = bin_num[len(bin_num) - 4:]
        bin_num = bin_num[:len(bin_num) - 4]
    else:
        act = '0' * (4 - len(bin_num)) + bin_num
        bin_num = ''
    # Without using a switch for the hexadecimal digits
    if act[0] == '0':  # Numbers of the form 0XXX, form 0 to 7 in hexadecimal
        n = 0
        for i in range(4):
            n += int(act[3 - i]) * (2 ** i)
        n = str(n)
    else:
        if act[1] == '0':
            if act[2] == '0':  # Numbers 100X, 8 or 9 in hexadecimal
                n = str(8 + int(act[0]) * (2 ** 1))
            else:
                if act[3] == '0':  # 1010, A in hexadecimal
                    n = 'A'
                else:  # 1011, B in hexadecimal
                    n = 'B'
        else:
            if act[2] == '0':
                if act[3] == '0':  # 1100, C
                    n = 'C'
                else:  # 1101, D
                    n = 'D'
            else:
                if act[3] == 0:
                    n = 'E'
                else:
                    n = 'F'
    resul = n + resul
if is_neg:
    resul = '-' + resul
print(resul)
