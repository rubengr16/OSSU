# Program which receives a file and search the spam confidence of each mail,
# it starts with 'X-DSPAM-Confidence:'. Get the floating number which follows
# and calculate the average of spam confidence
import sys

FILE_NAME = input("Enter the file's name: ")
count = 0
total_spam_confidence = 0

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    if line.startswith('X-DSPAM-Confidence:'):  # Searching condition
        count += 1  # Necessary to calculate the average
        total_spam_confidence += float(line[line.find(':') + 1:])
        # Get the floating point number

print('Average spam confidence:', total_spam_confidence / count)
