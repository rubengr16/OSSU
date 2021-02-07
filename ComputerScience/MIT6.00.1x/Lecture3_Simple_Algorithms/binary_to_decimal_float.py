# Converts a binary number (input) to decimal number
bin_num = input('Enter a binary number to convert to decimal: ')
print(bin_num, 'in decimal is', end=' ')
is_neg = None
resul = 0
p = len(str(int(float(bin_num) // 1))) - 1  # Keeps track of the value (2 ** p) of each binary digit

if bin_num[0] == '-':
    is_neg = True
    bin_num = bin_num[1:]  # Eliminates the '-'
    p -= 1  # The '-' does not count as binary value
else:
    is_neg = False

for c in bin_num:  # Iterates through bin_num and its digits
    if c != '.':
        resul += int(c) * (2 ** p)
        p -= 1

if is_neg:
    resul = -resul

print(resul)
