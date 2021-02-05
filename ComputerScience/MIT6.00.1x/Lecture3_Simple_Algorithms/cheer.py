# Cheers an entered word the times given by input, 
# it decides if the spell of each letter has "an" before or not
an_letters= 'aefhilmnorsxAEFHILMNORSX'

word = input('I will cheer for you! Enter a word: ')
times = int(input('Enthusiasm level: '))

for char in word:
    if char in an_letters:
        print('Give me an', char + '!', char)
    else:
        print('Give me a', char + '!', char)
        
print('What does that spell?')

for i in range(times):
    print(word + '!!!')