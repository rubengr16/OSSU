# Program which counts the appearances of each word in a file
import sys
import string

FILE_NAME = input("Enter the file's name: ")
counts = dict()  # Empty dictionary

try:
    f_in = open(FILE_NAME, 'r')  # open file handler
except FileNotFoundError:
    print('File not found:', FILE_NAME)
    sys.exit()


for line in f_in:
    line = line.rstrip()
    # Eliminate all types of blank spaces at the right
    line = line.translate(line.maketrans('', '', string.punctuation))
    # maketrans(fromstr, tostr, deletestr), fromstr is a string of characters
    # which need to be replaced, tostr is a string with the characters with
    # which will be replaced, deletestr specifies which characters to delete,
    # returns a dict with the correlation of the fromst characters (in unicode
    # values) as key andt heir corresponding replacement character (in unicode)
    # of the tostr as value, if there is no replacement character, it has None
    # (cases when the character is deleted). This dict is used to eliminate or
    # convert characters of the string of the string.translate()
    line = line.lower()  # Convert line to lower
    words = line.split()  # Divide line into a list
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)
