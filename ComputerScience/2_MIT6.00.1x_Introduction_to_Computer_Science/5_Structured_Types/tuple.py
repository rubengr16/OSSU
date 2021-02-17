# Tuple manipulation and usage
my_tuple = ()  # Empty tuple

my_tuple = (1, 'two', 3)  # tuple creation

print(my_tuple)  # tuple printing

# my_tuple[0] = 'one'  # Error, tuples are inmutable
my_tuple = ('one', 'two', 3)

resp = ''
for elem in my_tuple:  # tuple iteration
    resp += str(elem)

print(resp)

print(my_tuple)
print(my_tuple[:2])
