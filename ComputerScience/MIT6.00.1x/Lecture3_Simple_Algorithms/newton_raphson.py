# Calculation of roots throught Newton-Raphson method
# given a p(x) = a_n*x^n + a_n-1*x^n-1 + ...  + a_1*x^1 + a_0
# we want to find an r such as p(r) = 0.
# If g is an approximation, g - p(g) / p'(g) is a better aproximation
num = float(input('Enter a number to calculate the root: '))
guess = num / 2.0
epsilon = 0.001  # guess precission

while abs(guess * guess - num) >= epsilon:  # While guess is not enough good
    guess = guess - (((guess ** 2) - num) / (2 * guess))  # In this case for the square root: p(x) = x^2, p'(x) = 2*x

print('Square root of', str(num), 'is about', str(guess))
