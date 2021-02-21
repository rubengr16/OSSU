# Program which reads words from a file and stores them in a dictionary.
# Each key is the word, the value does not matters
import sys

FILE_NAME = input("Enter the file's name: ")
unique_words = dict()  # Empty dictionary

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    words = line.split()
    for word in words:
        if word not in unique_words:  # if word is not already added
            unique_words[word] = word

print(unique_words)
