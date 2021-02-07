# Converts a binary integer (input) to decimal integer
bin_num = input('Enter a binary integer to convert to decimal: ')
print(bin_num, 'in decimal is', end=' ')
is_neg = None
resul = 0
p = len(bin_num) - 1

if bin_num[0] == '-':
    is_neg = True
    bin_num = bin_num[1:]
    p -= 1
else:
    is_neg = False

for c in bin_num:
    resul += int(c) * (2 ** p)
    p -= 1

if is_neg:
    resul = -resul

print(resul)
