import random

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)



WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWord_l = list(''.join(secretWord))
    correct_guess = []
    for i in secretWord_l:
        if i in lettersGuessed:
            correct_guess.append(i)
    if set(correct_guess) == set(secretWord_l):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = {}
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            result[i] = secretWord[i]
        else:
            result[i] = '_'
    return ''.join(result.values())


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters ='abcdefghijklmnopqrstuvwxyz'
    availableLetters = list(''.join(letters))
    for l in availableLetters:
        if l in lettersGuessed:
            availableLetters.remove(l)
    return ''.join(availableLetters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    wordlen = len(secretWord)
    print("I am thinking of a word that is {} letters long.".format(wordlen))
    print('_' * wordlen)
    n = 8

    lettersGuessed = []
    while n > 0:
        if isWordGuessed(secretWord, lettersGuessed) == False:
            print('You have {} guesses left'.format(n))
            print('Available Letters: {}'.format(getAvailableLetters(lettersGuessed)))
            guessedLetter =input('Please guess a letter: ')
            guessedLetter.lower()
            if guessedLetter in lettersGuessed:
                print("You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            else:
                lettersGuessed.append(guessedLetter)
            print('letters have guessed are: {}'.format(lettersGuessed))
            if guessedLetter in secretWord:
                print('Good guess: {}'.format(getGuessedWord(secretWord,lettersGuessed)))
            else:
                print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord,lettersGuessed)))
                n -= 1
                if n ==0:
                    print("Sorry, you ran out of guesses. The word was {}".format(secretWord))
        else:
            print("Congratulations, you won!")
            break







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

if __name__ == '__main__':
    wordlist = loadWords()
    secretWord = chooseWord(wordlist)
    print('the secret word is: {}'.format(secretWord))
    hangman(secretWord)
