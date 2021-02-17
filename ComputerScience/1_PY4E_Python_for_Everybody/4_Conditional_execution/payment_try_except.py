# Asks for worked hours and the rate, and prints the payment.
# If there is not numerical input, try except manages
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    print('Pay:', hours * rate)
except ValueError:
    print('Error, please enter numeric input')
