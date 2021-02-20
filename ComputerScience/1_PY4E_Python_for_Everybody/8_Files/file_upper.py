# Program which receives a file and prints the contents of it (line by line)
# all in upper case
import sys

FILE_NAME = input("Enter the file's name: ")

try:
    f_in = open(FILE_NAME, 'r')
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    print(line.upper(), end='')
