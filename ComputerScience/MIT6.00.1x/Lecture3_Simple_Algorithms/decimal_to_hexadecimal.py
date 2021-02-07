# Receives an integer as input in decimal representation and converts it to hexadecimal
num = int(input('Enter an integer to convert to hexadecimal: '))
print(num, 'in hexadecimal is', end=' ')
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
        n = num % 16
        if n > 9:  # Switch for non-numerical hexadecimal representations
            if n == 10:
                n = 'A'
            elif n == 11:
                n = 'B'
            elif n == 12:
                n = 'C'
            elif n == 13:
                n = 'D'
            elif n == 14:
                n = 'E'
            elif n == 15:
                n = 'F'
        resul = str(n) + resul  # Process for conversion
        num //= 16
    if is_neg:
        resul = '-' + resul

print(resul)
