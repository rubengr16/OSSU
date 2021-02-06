# Receives an integer as input in decimal representation between -1 and 1 and converts it to binary
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
    is_neg = True
    intgr = abs(intgr)
else:
    is_neg = False

if intgr == 0:
    resul_intgr = '0'
else:
    if intgr != 0:
        while intgr > 0:
            resul_intgr = str(intgr % 2) + resul_intgr
            intgr //= 2

        if is_neg:
            resul_intgr = '-' + resul_intgr

if flt != 0:
    while (flt * (2 ** p)) % 1 > epsilon:
        p += 1

    flt = int(flt * (2 ** p))

    while flt > 0:
        resul_flt = str(flt % 2) + resul_flt
        flt //= 2

    print(str(resul_intgr) + '.' + '0' * (p - len(resul_flt)) + (resul_flt))
else:
    print(str(resul_intgr))
