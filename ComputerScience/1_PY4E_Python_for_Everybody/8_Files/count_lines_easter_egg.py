# Program which receives a file and counts its lines. If the file is called
# "na na boo boo" (our easter egg), it will print the name of the file in upper
# and  " - You have been punk'd"
import sys

FILE_NAME = input("Enter the file's name: ")
easter_egg = 'na na boo boo'
count = 0

if FILE_NAME == easter_egg:
    print(easter_egg.upper(), "- You have been punk'd")
else:
    try:
        f_in = open(FILE_NAME, 'r')  # File handler
    except FileNotFoundError:
        print('File not found:', FILE_NAME)
        sys.exit()

    for line in f_in:
        count += 1

    print('There were', count, 'subject lines in', FILE_NAME)
