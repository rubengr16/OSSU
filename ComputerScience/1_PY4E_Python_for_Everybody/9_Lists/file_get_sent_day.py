# Write a program which receives a file with the information of a mail box
# and prints the days when each email was sent
import sys

FILE_NAME = input("Enter the file's name: ")

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    words = line.split()  # split line through the spaces
    if len(words) > 0 and words[0] == 'From':
        # words is not empty and line begins with "From", where date appears
        print(words[2])
