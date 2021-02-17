# Calculation of the ns root through bisection search
x = int(input('Enter an integer: '))
p = int(input("Enter the number root's type: "))
epsilon = 0.01
guess = 0.0
low = 0.0
high = abs(x)  # For negative numbers calculations
num_guesses = 0

while abs(guess ** p - abs(x)) >= epsilon and guess <= abs(x):  # 2nd condition necessary to avoid endless loop
    if abs(guess ** p) < abs(x):  # Decides where to continue searching
        low = guess  # guess to the n is lower, we will search in the upper division
    else:
        high = guess  # If it is higher, we will search on the lower division
    guess = (low + high) / 2  # We make a guess which is on the half of the interval
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess ** p - abs(x)) >= epsilon:
    print('Failed on', p, 'root of', x)
else:
    if x < 0:
        guess = -guess
    print(guess, 'is close to the', p, 'root of', x)
