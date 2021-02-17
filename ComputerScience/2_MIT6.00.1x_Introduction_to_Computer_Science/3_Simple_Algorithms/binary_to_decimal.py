# Converts a binary integer (input) to decimal integer
bin_num = input('Enter a binary integer to convert to decimal: ')
print(bin_num, 'in decimal is', end=' ')
is_neg = None
resul = 0
p = len(bin_num) - 1  # Keeps track of the value (2 ** p) of each binary digit

if bin_num[0] == '-':
    is_neg = True
    bin_num = bin_num[1:]  # Eliminates the '-'
    p -= 1  # The '-' does not count as binary value
else:
    is_neg = False

for c in bin_num:  # Iterates through bin_num and its digits
    resul += int(c) * (2 ** p)
    p -= 1

if is_neg:
    resul = -resul

print(resul)
