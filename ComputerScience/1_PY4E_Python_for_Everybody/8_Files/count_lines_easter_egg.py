# Program which receives a file and prints the contents of it (line by line)
# all in upper case
import sys

FILE_NAME = input("Enter the file's name: ")
easter_egg = 'na na boo boo'
count = 0

if FILE_NAME == easter_egg:
    print(easter_egg.upper(), "- You have been punk'd")
else:
    try:
        f_in = open(FILE_NAME, 'r')
    except FileNotFoundError:
        print('File not found:', FILE_NAME)
        sys.exit()

    for line in f_in:
        count += 1

    print('There were', count, 'subject lines in', FILE_NAME)
