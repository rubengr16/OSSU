# Receives a program to prompt for a score between 0.0 and 1.0.
# Out of range prints 'Bad score'
# >= 0.9 A, >= 8 B, >= 0.7 C, >= 0.6 D, <0.6 F
try:
    score = float(input('Enter score: '))
    if 0.0 <= score and score <= 1.0:
        if score < 0.6:
            print('F')
        elif score < 0.7:
            print('D')
        elif score < 0.8:
            print('C')
        elif score < 0.9:
            print('B')
        else:
            print('A')
    else:
        print('Bad score')
except ValueError:
    print('Bad score')
