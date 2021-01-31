# Add the numbers from 0 to the end introduced by the user
end = int(input('Enter the end: '))
end2 = end
print('while')
total = 0
while end > 0:
   total += end
   end -= 1
print(total)

print()
print('for')
total = 0
for i in range(end2 + 1):
    total += i
print(total)