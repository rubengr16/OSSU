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
    resul = n + resul

if is_neg:
    resul = '-' + resul
print(resul)
