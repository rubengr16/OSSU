# Writing in a sample file

fwrite = open('file.txt', 'w')  # w sets the writing mode.
# a sets the append mode (write at the end of the file)

for i in range(10):
    word = input('Enter a word: ')
    fwrite.write(word + '\n')  # file.write() writes on the file,
    # \n is the new line character

fwrite.close()  # Always necessary to close all the files to save the progress
