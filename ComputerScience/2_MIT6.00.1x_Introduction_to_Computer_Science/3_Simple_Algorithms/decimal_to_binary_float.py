# Receives an integer as input in decimal representation and converts it to binary
num = float(input('Enter a number to convert to binary: '))
print(num, 'in binary is', end=' ')
resul_intgr = ''  # results are initialized as an empty string
resul_flt = ''
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
        while (flt * (2 ** p)) % 1 > epsilon:
            p += 1
        aux = int(aux * (2 ** p))

    if aux == 0:
        resul_aux = '0'
    while aux > 0:
        n = aux % 2
        resul_aux = str(n) + resul_aux  # Process for conversion
        aux //= 2

    if i == 0:
        if is_neg:
            resul_aux = '-' + resul_aux
        print(str(resul_aux), end='')
    elif resul_aux != '':
        print('.' + '0' * (p - len(resul_aux)) + (resul_aux))
