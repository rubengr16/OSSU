# Program whic counts how many emails where received (each message is started
# with a line started by "From ') and prints each sender (second word of the
# "From " line)
import sys

FILE_NAME = input("Enter the file's name: ")
count = 0

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    if line.startswith('From '):  # if the line is the separator one
        words = line.split()  # split the line's content into a list
        print(words[1])  # print the second line's element, the sender
        count += 1  # add to count a new message

print('There were', count, 'lines in the file with From as the first word')
