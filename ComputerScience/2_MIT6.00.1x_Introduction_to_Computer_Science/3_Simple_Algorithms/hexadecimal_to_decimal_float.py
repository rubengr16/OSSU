# Converts a hexadecimal number (input) to decimal number
hex_num = str(float(input('Enter a hexadecimal number to convert to decimal: ')))  # Unnecesary conversion, just for assuring '.' is included in the string
print(hex_num, 'in decimal is', end=' ')
is_neg = None
resul = 0
p = hex_num.find('.') - 1  # Keeps track of the value (16 ** p) of each hexadecimal digit

if hex_num[0] == '-':
    is_neg = True
    hex_num = hex_num[1:]  # Eliminates the '-'
    p -= 1  # The '-' does not count as hexadecimal value
else:
    is_neg = False

for c in hex_num:  # Iterates through hex_num and its digits
    if c != '.':
        if not c.isdigit():
            if c == 'A':
                c = 10
            elif c == 'B':
                c = 11
            elif c == 'C':
                c == 12
            elif c == 'D':
                c = 13
            elif c == 'E':
                c = 14
            elif c == 'F':
                c = 15
        resul += int(c) * (16 ** p)
        p -= 1

if is_neg:
    resul = -resul

print(resul)
