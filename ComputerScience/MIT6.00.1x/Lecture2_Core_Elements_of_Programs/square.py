# Squares a number through while loop

num = int(input('Enter a number: '))

resul = 0
i = 0

while i < num:
    resul += num
    i += 1
print('x * x =', resul)