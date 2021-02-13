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
