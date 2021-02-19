# Given a string through input, print it backwards
my_string = input('Enter something: ')

for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i], end='')  # print character at i index
