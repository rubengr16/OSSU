# Receives an integer as input in decimal representation between -1 and 1 and converts it to binary
num = float(input('Enter a number to convert to binary: '))
print(num, 'in binary is', end=' ')
resul = ''  # result is initialized as an empty string
is_neg = None
epsilon = 0.001
p = 0

if num < 0:
    is_neg = True  # Flag for negative
    num = abs(num)
else:
    is_neg = False

while (num * (2 ** p)) % 1 > epsilon:  # Calculates the power of 2 in order to have an accurate integral representation of the floating number
    p += 1

num = int(num * (2 ** p))  # Conversion to integer through power of 2

if num == 0:
    resul = '0'
else:
    while num > 0:
        resul = str(num % 2) + resul  # Decimal to binary power
        num //= 2

resul = '0.' + '0' * (p - len(resul)) + resul

if is_neg:
    resul = '-' + resul

print(resul)
