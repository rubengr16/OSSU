# Receives an integer as input in decimal representation and converts it to binary
num = int(input('Enter an integer to convert to binary: '))
print(num, 'in binary is', end=' ')
resul = ''  # result is initialized as an empty string
is_neg = None

if num < 0:
    is_neg = True  # Flag for negative number
    num = abs(num)
else:
    is_neg = False

if num == 0:
    resul = '0'
else:
    while num > 0:
        resul = str(num % 2) + resul  # Process for conversion
        num //= 2
    if is_neg:
        resul = '-' + resul

print(resul)
