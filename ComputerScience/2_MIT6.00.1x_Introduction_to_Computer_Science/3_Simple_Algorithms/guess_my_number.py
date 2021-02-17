# The user thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high (h) or too low (l) or correct (c)? (Other inputs are not understood)

print('Please think of a number between 0 and 100!')
guess = 100 / 2
low = 0
high = 100
resp = ''

while resp != 'c':
    print('Is your secret number', str(guess) + '?')
    resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if resp == 'l':
        low = guess
    elif resp == 'h':
        high = guess
    elif resp != 'c':
        print('Sorry, I did not understand your input.')
    guess = (high + low) / 2

print('Game over. Your secret number was:', guess)
