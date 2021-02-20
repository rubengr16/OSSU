# Program which reads numbers until the user enters "done".
# Once it is entered, prints out the maximum and minimum of the numbers.

minim, maxim = None, None
ans = None

while ans is None or ans != 'done':
    ans = input('Enter a number: ')
    try:
        ans = int(ans)
        if maxim is None or maxim < ans:
            maxim = ans
        if minim is None or minim > ans:
            minim = ans
    except ValueError:
        if ans != 'done':
            print('Invalid input')

print('Maximum is', maxim, '\nMinimum is', minim)
# \n is the new line character
