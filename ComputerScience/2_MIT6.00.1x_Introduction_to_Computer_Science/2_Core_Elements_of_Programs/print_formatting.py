# print your favorite number in different formats
num = float(input('Enter your favorite number: '))

print('My favorite number is', num, '.', 'num =', num)  # Each , enters a space between the strings
print('My favorite number is' + str(num) + '.' + 'num =' + str(num))  # + concatenates strings directly without any separator