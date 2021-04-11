# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """

    Returns
    -------
    wordList : list
        List of valid words. Words are strings of lowercase letters.

    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')  # Open file
    # wordList: list of strings
    wordList = []
    for line in inFile:  # for each line
        wordList.append(line.strip().lower())
        # Divide the line and add each element to the list
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """

    Parameters
    ----------
    sequence : string or list
        Words.

    Returns
    -------
    freq : dictionary
        Keys are elements of the sequence
        and the values are integer counts, for the number of times that
        an element is repeated in the sequence.

    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
        # if the key exists, returns it freq and adds one,
        # otherwise, return 0 and adds 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """

    Parameters
    ----------
    word : string
        Word, a string in lowercase.
    n : integer
        Word's size.

    Returns
    -------
    score: int >= 0
    Score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES.get(letter, 0)
        # Get the letter value from the dictionary and add to the score

    score *= len(word)
    # The addition of the score of each letter is multiplied by the word's size

    if len(word) == n:
        score += 50  # if the word uses all the letters, add 50 extra points

    return score


#
# Problem #2: Make sure you understand how this function works and what it does
#
def displayHand(hand):
    """

    Parameters
    ----------
    hand : dictionary
        string:int pairs.

    Returns
    -------
    None.

    Output
    ------
     Displays the letters currently in the hand. The order of the letters is
     unimportant.

    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print on the same line, blank separator
    print()  # print an empty line


#
# Problem #2: Make sure you understand how this function works and what it does
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]  # From 0 until len
        hand[x] = hand.get(x, 0) + 1  # Set the freq

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """

    Parameters
    ----------
    hand : dictionary
        string:int pairs. Contains the letter which the user can make words
        with and its frequencies.
    word : string
        Word made by the user.

    Returns
    -------
    hand_mod : dictionary
        string:int pairs. It updates the hand:  uses up the letters in the
        given word and returns the new hand, without those letters in it.
        Has no side effects: does not modify hand.

    """
    hand_mod = hand.copy()  # copy the hand in order to not modify it
    aux = []

    for letter in word:
        hand_mod[letter] -= 1  # Delete from freq the letters used

    for key in hand_mod:
        if hand_mod[key] == 0:
            aux += [key]  # Search for the keys with freq == 0

    for key in aux:
        del(hand_mod[key])  # Delete elements with freq == 0

    return hand_mod


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    fail = False

    if word not in wordList:
        fail = True
    else:
        aux = getFrequencyDict(word)
        keys = list(aux.keys())
        i = 0

        while i < len(keys) and not fail:
            if keys[i] not in hand.keys():
                fail = True
            elif aux[keys[i]] > hand[keys[i]]:
                fail = True
            i += 1

    return not fail


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0

    for k in hand:
        length += hand[k]

    return length


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # Keep track of the total score
    score = 0
    word = None
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) and word != '.':  # if word is '.' break
        # Display the hand
        print('Current Hand: ', end='')
        displayHand(hand)
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word != '.':
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word(print a message followed by a blank line)
                print('Invalid word, please try again.')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned,
                # and the updated total score, in one line followed by
                # a blank line
                score += getWordScore(word, n)
                print('"' + word + '" earned:', getWordScore(word, n),
                      'points. Total:', score)
                # Update the hand
                hand = updateHand(hand, word)
    # Game is over (user entered a '.' or ran out of letters),
    # so tell user the total score
    if word == '.':
        print('Goodbye! Total score:', score)
    else:
        print('Run out of letters. Total score:', score)


#
# Problem #5: Playing a game
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    ans = None
    hand = None
    while ans != 'e' or ans is None:
        ans = input('Enter n to deal a new hand, r to replay the last hand, ' +
                    'or e to end game: ')
        if ans == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif ans == 'r':
            if hand is None:
                print('You have not played a hand yet. ' +
                      ' Please play a new hand first!')
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif ans != 'e':
            print('Invalid command.')


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
