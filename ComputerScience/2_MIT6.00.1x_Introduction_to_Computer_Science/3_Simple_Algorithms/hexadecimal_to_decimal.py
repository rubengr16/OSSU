# Converts a binary integer (input) to decimal integer
hex_num = input('Enter a hexadecimal integer to convert to decimal: ')
print(hex_num, 'in decimal is', end=' ')
is_neg = None
resul = 0
p = len(hex_num) - 1  # Keeps track of the value (2 ** p) of each binary digit

if hex_num[0] == '-':
    is_neg = True
    hex_num = hex_num[1:]  # Eliminates the '-'
    p -= 1  # The '-' does not count as binary value
else:
    is_neg = False

for c in hex_num:  # Iterates through hex_num and its digits
    if not c.isdigit():  # If the hexadecimal value is a letter, we create a switch for the conversion
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
