# Receives an integer as input in decimal representation between -1 and 1 and converts it to binary
num = float(input('Enter a number to convert to binary: '))
print(num, 'in binary is', end=' ')
resul = ''  # result is initialized as an empty string
is_neg = None
epsilon = 0.001
p = 0

if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False

if int(num) == 0:
    is_lower = True
else:
    is_lower = False

while (num * (2 ** p)) % 1 > epsilon:
    p += 1

num = int(num * (2 ** p))

if num == 0:
    resul = '0'
else:
    while num > 0:
        resul = str(num % 2) + resul
        num //= 2

resul = '0.' + '0' * (p - len(resul)) + resul

if is_neg:
    resul = '-' + resul

print(resul)
