# Program which reads numbers until the user enters "done".
# Once it is entered, prints out the maximum and minimum of the numbers.

nums = list()  # Empty list

while len(nums) < 1 or nums[-1] != 'done':
    nums += [input('Enter a number: ')]
    try:
        nums[-1] = int(nums[-1])
    except ValueError:
        if nums[-1] != 'done':  # if num[-1] == 'done', there is no prompt
            print('Invalid input')
            nums = nums[:-1]  # Elimination of the invalid element

nums = nums[:-1]
# Loop exit through 'done', 'done' was added to the list, we have to delete it
print('Maximum is', max(nums), '\nMinimum is', min(nums))
# \n is the new line character
