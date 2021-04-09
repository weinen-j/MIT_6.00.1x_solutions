# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    slist = list(secretWord)
    for i in lettersGuessed:
        while i in slist:
            slist.remove(i)
    if len(slist) == 0:
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
    slist = list(secretWord)
    dummy = list(slist)
    for i in lettersGuessed:
        while i in dummy:
            dummy.remove(i)

    for i in dummy:
        while i in slist:
            pos = slist.index(i)
            slist[pos] = "_"

    slist = " ".join(slist)
    return slist


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = list(string.ascii_lowercase)
    for i in lettersGuessed:
        letters.remove(i)
    letters = "".join(letters)
    return letters


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

    mistakes = 0
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")

    while not isWordGuessed(secretWord, lettersGuessed):
        if mistakes >= 8:
            break
        print("-----------")
        print("You have " + str(8 - mistakes) + " guesses left")
        print("Available Letters: " + str(getAvailableLetters(lettersGuessed)))
        guess = input("Please guess a letter: ")
        guess = guess.lower()

        if len(guess) == 1 and isinstance(guess, str):

            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: "
                      + str(getGuessedWord(secretWord, lettersGuessed)))
            elif guess not in secretWord:
                lettersGuessed.append(guess)
                mistakes += 1
                print("Oops! That letter is not in my word: "
                      + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                lettersGuessed.append(guess)
                print("Good guess: "
                      + str(getGuessedWord(secretWord, lettersGuessed)))

    print("-----------")
    if mistakes < 8:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
