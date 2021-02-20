# Program which receives a file and prints the contents of it (line by line)
# all in upper case
import sys

FILE_NAME = input("Enter the file's name: ")

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:  # Gets each line of the file until it is finished
    print(line.upper(), end='')
    # print each line in upper, without default print new line, as each line
    # on the file has a '\n' at its end
