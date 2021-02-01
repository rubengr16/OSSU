# The user enters a string and finds the longest substring ordered alphabetically 
# (if two letters are equal, they are also ordered)
string = input('Enter a string: ')
actual_ordered = string[0]
max_ordered = string[0]

for i in range (1, len(string)):
    if string[i - 1] <= string[i]:
        actual_ordered += string[i]
    else:
        actual_ordered = string[i]
    if len(actual_ordered) > len(max_ordered):
        max_ordered = actual_ordered
        
print('Longest substring in alphabetical order is:', max_ordered)
