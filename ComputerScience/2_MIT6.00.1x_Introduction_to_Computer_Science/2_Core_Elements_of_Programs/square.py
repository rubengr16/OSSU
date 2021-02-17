# Squares a number through while loop

num = int(input('Enter a number: '))

resul = 0
i = 0

print('while')
while i < num:
    resul += num
    i += 1
print('x * x =', resul)

print()
print('for')
resul = 0
for i in range(num):
    resul += num
print('x * x =', resul)