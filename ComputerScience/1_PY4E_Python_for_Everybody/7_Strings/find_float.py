# Receiving a str with 'X-DSPAM-Confidence: ' concatenated with a float in str.
# Returns the floating point number in float.
my_string = 'X-DSPAM-Confidence: ' + input('Enter a float: ')

my_float = float(my_string[my_string.find(':') + 1:])
# Position of the ':' + 1 to eliminate that character and keep only the number,
# float() eliminates the spaces of the str and cast only digits
print('Your float is:', str(my_float) + '. Its type is:', type(my_float))
