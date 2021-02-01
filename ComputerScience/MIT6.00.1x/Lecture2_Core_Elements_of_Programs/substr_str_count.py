# Receives through input a string and a substring, 
# prints out the mumber of repetitions of the substring if it is contained on the string
string = input('Enter a string: ')
substring = input('Enter a substring: ')  
count = 0

for i in range(len(string)):
    j = 0
    while j < len(substring) and (j + i) < len(string) and substring[j] == string[j + i]:
        j += 1
    if j == len(substring):
        count += 1
print('Number of times', substring, 'occurs is:', count)