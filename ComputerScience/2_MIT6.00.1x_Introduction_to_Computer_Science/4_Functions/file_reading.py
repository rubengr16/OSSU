# Reading a sample file

fread = open('file.txt', 'r')  # r sets the read mode

for line in fread:  # Goes through all the lines on the file
    print(line, end='')  # Prints each line

fread.close()  # Always necessary to close all the files to protect the file
