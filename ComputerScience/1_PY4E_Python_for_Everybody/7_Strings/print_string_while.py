# Given a string through input, print it backwards
my_string = input('Enter something: ')
i = len(my_string) - 1

while i >= 0:
    print(my_string[i], end='')  # print character at i index
    i -= 1  # decreases the index (i)
