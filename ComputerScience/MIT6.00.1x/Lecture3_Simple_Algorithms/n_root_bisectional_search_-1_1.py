# Calculation of the n root through bisection search
x = float(input('Enter a float between -1 and 1: '))
p = int(input("Enter the number root's type: "))
epsilon = 0.0001
guess = 0.0
low = abs(x)  # If we search for guesses lower than abs(x) we will obtain a lower value than abs(x)
high = 1  # The root can't be greater than 1
num_guesses = 0

while abs(guess ** p - abs(x)) >= epsilon and guess <= 1:  # 2nd condition necessary to avoid endless loop
    if abs(guess ** p) < abs(x):  # Decides where to continue searching
        low = guess  # guess to the square is lower, we will search in the upper division
    else:
        high = guess  # If it is higher, we will search on the lower division
    guess = (low + high) / 2  # We make a guess which is on the half of the interval
    num_guesses += 1
    print(guess)

print('num_guesses =', num_guesses)

if abs(guess ** p - abs(x)) >= epsilon:
    print('Failed on', p, 'root of', x)
else:
    if x < 0:
        guess = -guess
    print(guess, 'is close to the', p, 'root of', x)
