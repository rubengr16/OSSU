# Taking characters through their index
user = input('Enter your name: ')

print('Character 3:', user[2])  # Index starts at 0 and ends at length - 1
print('Last character:', user[-1])  # Searchs for the character in length - 1 position
print('Characters from 2 to 3:', user[1:3])  # The last index character is excluded
print('Characters from the beginning to 3:', user[:2])
print('Characters form 3 to the end:', user[2:])
print('A copy of the string:', user[:])
print('Characters from the beginning to the end in the odd positions:', user[::2])  # The 3rd argument tells us the step size
print('Characters from the beginning to the end inverted:', user[::-1])
