# Receives an integer as input in decimal representation and converts it to hexadecimal
num = float(input('Enter a number to convert to hexadecimal: '))
print(num, 'in hexadecimal is', end=' ')
resul = ''  # result is initialized as an empty string
intgr = int(num)
flt = num - intgr
is_neg = None
epsilon = 0.001
p = 0

if intgr < 0:
    is_neg = True  # Flag for negative number
    intgr = abs(intgr)
    flt = abs(flt)
else:
    is_neg = False

for i in range(2):
    resul_aux = ''  # result_aux is initialized as an empty string
    if i == 0:
        aux = intgr
    else:
        aux = flt
        while (aux * (16 ** p)) % 1 > epsilon:
            p += 1
        aux = int(aux * (16 ** p))

    if aux == 0:
        resul_aux = '0'
    while aux > 0:
        n = aux % 16
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
        resul_aux = str(n) + resul_aux  # Process for conversion
        aux //= 16

    if i == 0:
        if is_neg:
            resul_aux = '-' + resul_aux
        print(str(resul_aux), end='')
    elif resul_aux != '':
        print('.' + '0' * (p - len(resul_aux)) + (resul_aux))
