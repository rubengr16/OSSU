# Hangman game

import random  # Random select of words
import string  # string_name.replace(substr1, substr2)


def loadWords():
    """

    Returns
    -------
    wordlist : list
        Valid words as elements, they are strings of lowercase letters.

    """
    print('Loading word list from file...')
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')  # Read mode
    # line: string
    line = inFile.readline()  # Take 1 line of the file's input
    # wordlist: list of strings
    wordlist = line.split()  # Divide the line through spaces
    print("  ", len(wordlist), 'words loaded.')
    inFile.close()  # Convenient to close all files
    return wordlist


def chooseWord(wordlist):
    """

    Parameters
    ----------
    wordlist : list
        Elements are words (str).

    Returns
    -------
    str
        Word from wordlist at random.

    """
    return random.choice(wordlist)  # random module picks a word


def isWordGuessed(secret_word, letters_guessed):
    """

    Parameters
    ----------
    secret_word : str
        Word the user is guessing.
    letters_guessed : list
        Elements of type char, what letters have been guessed so far.

    Returns
    -------
    bool
       True if all the letters of secretWord are in lettersGuessed;
       False otherwise.

    """
    i = len(secret_word) - 1

    while secret_word[i] in letters_guessed and i >= 0:
        i -= 1

    if i == -1:  # All the secret_words are in letters_guessed
        return True
    else:  # Some letters are not guessed
        return False


def getGuessedWord(secret_word, letters_guessed):
    """

    Parameters
    ----------
    secret_word : str
        Word the user is guessing..
    letters_guessed : list
        Elements of char, what letters have been guessed so far.

    Returns
    -------
    word_guess : str
        Letters and underscores that represents what letters in secretWord
        have been guessed so far.

    """
    word_guess = ''

    for c in secret_word:
        if c in letters_guessed:  # We have guessed that letter
            word_guess += c
        else:  # We have not, so it remains unknown
            word_guess += '_ '

    return word_guess


def getAvailableLetters(letters_guessed):
    """

    Parameters
    ----------
    letters_guessed : list
        Elements of type char, what letters have been guessed so far..

    Returns
    -------
    letters_available : str
        Comprised of letters that represents what letters have not
        yet been guessed.

    """
    letters_available = string.ascii_lowercase  # Get the alphabet

    for letter in letters_guessed:
        letters_available = letters_available.replace(letter, '')
        # Eliminate the letter from the alphabet as it is chosen

    return letters_available


def hangman(secret_word):
    """


    Parameters
    ----------
    secret_word : str
        Secret word to guess.

    Output
    ------
     Starts up an interactive game of Hangman.

        * At the start of the game, let the user know how many
          letters the secretWord contains.

        * Ask the user to supply one guess (i.e. letter) per round.

        * The user should receive feedback immediately after each guess
          about whether their guess appears in the computers word.

        * After each round, you should also display to the user the
          partially guessed word so far, as well as letters that the
          user has not yet guessed. Starts up an interactive game of Hangman.

        * At the start of the game, let the user know how many
          letters the secretWord contains.

        * Ask the user to supply one guess (i.e. letter) per round.

        * The user should receive feedback immediately after each guess
          about whether their guess appears in the computers word.

        * After each round, you should also display to the user the
          partially guessed word so far, as well as letters that the
          user has not yet guessed.

    Game ends when 8 incorrect guesses has been made or the word is guessed.

    Returns
    -------
    None.

    """
    guesses = 8
    letters_guessed = []
    available_let = None
    c = None

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')

    while guesses > 0 and not isWordGuessed(secret_word, letters_guessed):
        # We have guesses remaining and we haven guessed the word correcty
        print('-' * 11)
        print('You have', guesses, 'guesses left.')
        available_let = getAvailableLetters(letters_guessed)
        print('Available letters:', available_let)
        c = input('Please guess a letter: ').lower()  # Ensure lower case input

        if c in available_let:  # Guess letter is not chosen
            letters_guessed += c  # Add to the chosen registry
            if c in secret_word:  # Guess letter is in the secret_word
                print('Good guess:',
                      getGuessedWord(secret_word, letters_guessed))
            else:  # Bad guess letter
                print("Oops! That letter is not in my word:",
                      getGuessedWord(secret_word, letters_guessed))
                guesses -= 1  # One guess left less
        else:  # Guess letter is already chosen
            print("Oops! You've already guessed that letter:",
                  getGuessedWord(secret_word, letters_guessed))

    print('-' * 11)
    if isWordGuessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word + '.')


WORDLIST_FILENAME = 'words.txt'
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
