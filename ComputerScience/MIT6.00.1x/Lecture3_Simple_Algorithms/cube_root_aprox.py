# Calculates an aproximate cube root solution with an error called epsilon
cube = int(input('Enter an integer: '))
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess ** 3 - abs(cube)) >= epsilon and guess <= abs(cube):  # 2nd condition necessary to avoid endless loop
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess ** 3 - abs(cube)) >= epsilon:
    print('Failed on cube root of', cube)
else:
    if cube < 0:
        guess = -guess
    print(guess, 'is close to the cube root of', cube)
    