# Find all the unique words in a file, then sort and print them
import sys

FILE_NAME = input("Enter the file's name: ")
unique_words = list()  # Empty list creation

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()

for line in f_in:
    words = line.split()
    for word in words:
        if word not in unique_words:  # this word is not already added
            unique_words.append(word)

unique_words.sort()
print(unique_words)
