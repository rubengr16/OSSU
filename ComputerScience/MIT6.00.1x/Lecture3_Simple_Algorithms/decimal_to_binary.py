# Receives an integer as input in decimal representation and converts it to binary
num = int(input('Enter a number to convert to binary: '))
print(num, 'in binary is', end=' ')
resul = ''  # result is initialized as an empty string

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

if num == 0:
    resul = '0'
else:
    while num > 0:
        resul = str(num % 2) + resul
        num //= 2
    if isNeg:
        resul = '-' + resul

print(resul)
