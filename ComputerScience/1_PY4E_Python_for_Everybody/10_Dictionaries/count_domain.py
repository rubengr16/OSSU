# Program which counts how many emails where received from each domain name
# (part after the '@' of the second word in each line started by "From ',
# as each message is delimited by this start)
import sys

FILE_NAME = input("Enter the file's name: ")
count = dict()

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    if line.startswith('From '):  # if the line is the separator one
        words = line.split()  # split the line's content into a list
        if len(words) > 2:
            domain = words[1][words[1].find('@') + 1:]
            count[domain] = count.get(domain, 0) + 1
            # Sender is the second word, domain is after the '@'.
            # dict.get(key, default) searchs if there is already this key in
            # the dictionary, if it exist returns the value,
            # if not returns default

print(count)
