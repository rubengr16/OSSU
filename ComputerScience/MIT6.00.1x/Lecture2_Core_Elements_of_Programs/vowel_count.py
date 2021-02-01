# Given a string through input, counts how many vowels there are
# (valid vowels: 'a', 'e', 'i', 'o', 'u')
string = input('Enter a string: ')
vowels = 0

for l in string:
    if l == 'a' or l == 'e'or l == 'i' or l == 'o' or l == 'u':
        vowels += 1
print('Number of vowels:', vowels)