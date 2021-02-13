# Dictionaries are interesting to index items
# of interest directly (not always int). key:value pairs.
# Manipulation and usage of them
my_dict = {}  # Empty dictionary

# keys: must be unique, inmutable type (hashable),
# values: any type (inmutable and mutable), can be duplicates.
# No order to keys or values.
grades = {'F.C.': 9.3, 'F.P': 9.3, 'T.P': 9.6, 'T.S.O.': 7.4}
grades['A.M.'] = 7.4  # Dictionaries are mutable
grades['L.'] = 8.7

print('Is A.M. in grades:', 'A.M.' in grades)
print('Is M. in grades:', 'M.' in grades)

del(grades['F.C.'])  # Delete a entry of the directory through its key

print('grades keys:', grades.keys())  # Returns an iterable that works as tuple

print('grades values:', grades.values())  # Returns an iterable
