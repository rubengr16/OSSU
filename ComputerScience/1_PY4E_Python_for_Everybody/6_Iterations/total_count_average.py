# Program which reads numbers until the user enters "done".
# Once it is entered, prints out the total, count and average of the numbers.

total, count = 0, 0  # Initialize 2 variables at the same time
ans = None

while ans is None or ans != 'done':
    try:
        ans = input('Enter a number: ')
        ans = int(ans)  # Try to cast the input
        total += ans
        count += 1
    except ValueError:  # input's cast error
        print('Invalid input')
        continue

print('total:', total, ', count:', count, ' average:', total / count)
