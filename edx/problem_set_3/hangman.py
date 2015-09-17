# 6.00 Problem Set 3
# 
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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    guessed_word = ""
    for i in secretWord:
        if i in lettersGuessed:
            guessed_word += i
        else:
            guessed_word += "_"
    return secretWord == guessed_word




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ""
    for i in secretWord:
        if i in lettersGuessed:
            guessed_word += i
        else:
            guessed_word += "_"
    return guessed_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    new_availbale_letters = []
    for c in available_letters:
        if c not in lettersGuessed:
            new_availbale_letters.append(c)
    return "".join(new_availbale_letters)
    

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
    print secretWord
    length = len(secretWord)
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is",length,"letters long."
    print "-------------"
    index = 8
    guessed_letters = []
    while index > 0:
        print "You have",index,"guesses left."
        print "Available letters:", getAvailableLetters(guessed_letters)
        guessed_letter = raw_input("Please guess a letter:").lower()
        if guessed_letter in guessed_letters:
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, guessed_letters)
            print "------------"
            continue
        else:
            guessed_letters.append(guessed_letter)
        if secretWord.find(guessed_letter) != -1:
            #print "guessed_letters :",guessed_letters
            print "Good guess:", getGuessedWord(secretWord, guessed_letters)
        else:
            index -= 1
            print "Oops! That letter is not in my word:", getGuessedWord(secretWord, guessed_letters)
        print "------------"
        if isWordGuessed(secretWord, guessed_letters):
            print "Congratulations, you won!"
            break
    if not isWordGuessed(secretWord, guessed_letters):
        print "Sorry, you ran out of guesses. The word was", secretWord+"."








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman("y")