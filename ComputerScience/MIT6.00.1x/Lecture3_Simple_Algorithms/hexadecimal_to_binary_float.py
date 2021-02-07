# Converts a hexadecimal number (input) to binary number
hex_num = input('Enter a hexadecimal number to convert to binary: ')  # Unnecesary conversion, just for assuring '.' is included in the string
print(hex_num, 'in decimal is', end=' ')
is_neg = None
resul = ''


if hex_num[0] == '-':
    is_neg = True
    hex_num = hex_num[1:]  # Eliminates the '-'
else:
    is_neg = False

for c in hex_num:
    if c.isdigit():
        c = int(c)
        aux = ''
        while c > 0:
            aux = str(c % 2) + aux  # Process for conversion
            c //= 2
        resul += ('0' * (4 - len(aux)) + aux)  # Addition of 0s to complete the four bits represented in hexadecimal, + ' ' could be added to make a separation
    else:  # switch for non-numerical hexadecimal digits
        if c == 'A':
            c = '1010'
        elif c == 'B':
            c = '1011'
        elif c == 'C':
            c = '1100'
        elif c == 'D':
            c = '1101'
        elif c == 'E':
            c = '1110'
        elif c == 'F':
            c = '1111'
        resul += c  # + ' ' could be added to make a separation between each 4 bits

if is_neg:
    resul = '-' + resul
print(resul)
