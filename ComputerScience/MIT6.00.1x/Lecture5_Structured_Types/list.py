# List manipulation and usage

my_list = []  # Empty list


for i in range(50):
    if i == 0:
        my_list += [200]
    else:
        my_list += [i]  # list concatenation

my_list[0] = 0  # list are mutable

total = 0
for elem in my_list:
    if elem != my_list[0]:
        print('+', end=' ')
    total += elem
    print(elem, end=' ')

print('=', total)

my_list.append(50)  # Adds the given element to the end of the list

my_list += [52, 53, 54]  # Concatenates the given lists in the given order

my_list.extend([55, 56, 57, 58, 59])  # Mutates my_list to the same elements
# but adding the given ones

my_list.remove(0)  # Removes the first appearance of an element with value 0,
# if there are more elements with the given value, only removes the first

del(my_list[12])  # Removes the element at the given index

my_list.pop()  # Returns the last element
# and mutates to a list without the last element,
# if an index is given, eliminates the element at it

my_string = ' '.join(str(my_list))  # Join a list with the given separator
print('my_string:', my_string)
# Split a str dividing by the given separator
print('my_string splitted as list:', my_string.split(' '))


my_list += [-100]
print('my_list:', my_list)

# Sort a list without mutation
print('my_list sorted and not mutated:', sorted(my_list))
my_list.reverse()  # Mutate list ordering reverse its elements by its index
print('my_list sorted and mutated:', my_list)
my_list.sort()  # Mutate list sorting its elements by the value
print('my_list reversed and mutated:', my_list)

print()
print('Alias:')
print('-' * 79)
my_list_copy = my_list  # Alias for the same string
print('my_list:', my_list)
print('my_list_copy:', my_list_copy)

print('modified')
my_list_copy += [100]
# Notice both have mutated, as they have a pointer to the same list
print('my_list:', my_list)
print('my_list_copy:', my_list_copy)

print('Real copy:')
print('-' * 79)
my_list_copy.remove(100)  # my_list and alias points to the list before alias
print('my_list:', my_list)
print('my_list_copy:', my_list_copy)

print('copied')
my_list_copy = my_list[:]  # Copy the elements and not the pointer
print('my_list:', my_list)
print('my_list_copy:', my_list_copy)
