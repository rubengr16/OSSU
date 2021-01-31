# CUbe root by guess and check
num = int(input('Enter number: '))
x = 0

print('while')
while x ** 3 < abs(num):
    x += 1
if x ** 3 == abs(num):
    print(x, 'and', -x, 'are the cube root of', num)
else:
    print(num, 'is not a perfect cube')
    
print('for')
for x in range(abs(num) + 1):
    if x ** 3 == abs(num):
        break
if x ** 3 >= abs(num):
    print(x, 'and', -x, 'are the cube root of', num)
else:
    print(num, 'is not a perfect cube')