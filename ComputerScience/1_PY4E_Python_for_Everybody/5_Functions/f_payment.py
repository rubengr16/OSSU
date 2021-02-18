# Function which asks for worked hours and the rate , and prints the payment:
# normal hours are multiplied by rate, extra ones (> 40) by rate * 1.5
def payment(hours, rate):
    overtime = 0
    if hours > 40:
        overtime = hours - 40
        hours = 40
    print('Pay:', (hours + overtime * 1.5) * rate)


hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
payment(hours, rate)
