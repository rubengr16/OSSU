# Usage of random module
import random

print(random.random)
for _ in range(10):
    print(random.random())
    # Print float random numbers from 0.0 included and 1.0 excluded

print('-' * 79)
print('random.randint')
for _ in range(10):  # _ as the the iterative variable's value is not important
    print(random.randint(-10, 10))
    # Print int random numbers from the first argument to the last included

print('-' * 79)
print('random.choice')
my_string = input('Enter something: ')
for _ in range(10):
    print(random.choice(my_string))
    # Given a sequence, print randomly its elements
