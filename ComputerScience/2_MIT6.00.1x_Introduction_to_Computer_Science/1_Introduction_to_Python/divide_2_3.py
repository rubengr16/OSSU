# Number is divisible by 2 and/or 3
num = int(input('Enter a number: '))

if num % 2 == 0:
    if num % 3 == 0:  # Nested conditional
        print(num, 'is divisible by 2 and 3')
    else:
        print(num, 'is divisible by 2 and not by 3')
elif num % 3 == 0:
    print(num, 'is divisible by 3 and not by 2')
