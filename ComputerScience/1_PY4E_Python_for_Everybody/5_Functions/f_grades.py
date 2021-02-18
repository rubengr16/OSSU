# Receives a program to prompt for a score between 0.0 and 1.0.
# Out of range prints 'Bad score'
# >= 0.9 A, >= 8 B, >= 0.7 C, >= 0.6 D, < 0.6 F
def grades(score):
    """

    Parameters
    ----------
    score : float
        Grade between 0.0 and 1.0.

    Returns
    -------
    score : str
        If score >= 0.9 A, elif >= 8 B, elif >= 0.7 C, elif >= 0.6 D,
        elif < 0.6 F. Otherwise, if grade is < 0.0 or > 1.0 'Bad score'.

    """
    if 0.0 <= score and score <= 1.0:
        if score < 0.6:
            score = 'F'
        elif score < 0.7:
            score = 'D'
        elif score < 0.8:
            score = 'C'
        elif score < 0.9:
            score = 'B'
        else:
            score = 'A'
    else:
        score = 'Bad score'
    return score


try:
    score = float(input('Enter score: '))
    print(grades(score))
except ValueError:
    print('Bad score')
