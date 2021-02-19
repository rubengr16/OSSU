# Hello world formatting
try:
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    print('Hello %s, you have %d' % (name, age))
    # %s stands for string, %d or %i for decimal, %g or %f for float
except ValueError:
    print('Invalid input')

print('kk %f' % 0.1)
