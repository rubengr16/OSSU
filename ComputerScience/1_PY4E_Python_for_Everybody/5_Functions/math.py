# Usage of math module
import math

print(math)  # print information associated with the module


try:
    signal_power = float(input('Enter the signal power: '))
    noise_power = float(input('Enter the noise power: '))
    ratio = signal_power / noise_power
    decibels = 10 * math.log10(ratio)  # Decibels calculations formula
    print('The decibels are:', decibels)
except ValueError:
    print('Invalid Data')


try:
    radians = float(input('Enter the radians: '))
    height = math.sin(radians)
    print('The height is', height)
except ValueError:
    print('Invalid Data')

try:
    degrees = float(input('Enter the degrees: '))
    radians = degrees / 360.0 * 2 * math.pi  # Degrees to radians formula
    height = math.sin(radians)
    print('The height is', height)
except ValueError:
    print('Invalid Data')

print(math.sqrt(16))  # Calculate the square root of a number
