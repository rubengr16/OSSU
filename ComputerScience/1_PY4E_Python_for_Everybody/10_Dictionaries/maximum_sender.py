# Program searchs for the sender with more messages in the inbox
import sys

FILE_NAME = input("Enter the file's name: ")
count = dict()  # Empty dictionary
max_sender = None
max_times = None

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    if line.startswith('From '):  # if the line is the separator one
        words = line.split()  # split the line's content into a list
        if len(words) > 3:
            count[words[1]] = count.get(words[1], 0) + 1
            # Day is the third word.
            # dict.get(key, default) searchs if there is already this key in
            # the dictionary, if it exist returns the value,
            # if not returns default

for sender, times in count.items():
    if max_times is None or times > max_times:
        max_times = times
        max_sender = sender

print('Maximum sender is', str(max_sender) + ', with', max_times, 'times.')
