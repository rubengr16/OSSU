# Program which counts how many emails where received (each message is started
# with a line started by "From ') and prints each sender (second word of the
# "From " line)
import sys

FILE_NAME = input("Enter the file's name: ")
count = dict()  # Empty dictionary

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    if line.startswith('From '):  # if the line is the separator one
        words = line.split()  # split the line's content into a list
        if len(words) > 3:
            count[words[2]] = count.get(words[2], 0) + 1
            # Day is the third word.
            # dict.get(key, default) searchs if there is already this key in
            # the dictionary, if it exist returns the value,
            # if not returns default


print(count)
