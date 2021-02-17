# comparation betwee 3 numbers
x = -10
y = 10
num = int(input('Enter a number: '))

print()
print('Which is least?')
print('num =', num, 'x =', x, 'y =', y)
print()

if num < y and num < x:  # Compound booleans
    print('num =', num, 'is the least')
elif y < x:
    print('y =', y, 'is the least')
else:
    print('x =', x, 'is the least')