# 6.00 Problem Set 3
# Hangman game
# Jaskirat Singh
# 20 October, 2012

import random
import string

WORDLIST_FILENAME = "words.txt"
MAX_GUESSES = 8

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
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord = list(secretWord)
    index = -1
    for char in secretWord:
        index += 1
        if char not in lettersGuessed:
            secretWord[index] = '_ '
    return ''.join(secretWord)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = list(string.lowercase[0:26])
    index = -1
    for char in availableLetters:
        index += 1
        if char in lettersGuessed:
            availableLetters[index] = ''
    return ''.join(availableLetters)
    

def hangman(secretWord):
    guessLeft = MAX_GUESSES
    lettersGuessed = []
    
    #welcome the player
    print 'Welcome to the game, Hangman'
    print 'I am thinking of a word that is', len(secretWord) , 'letters long'

    #begin game
    while guessLeft > 0:
        print '-'*12
        print 'You have', guessLeft, 'guesses left.'
        print 'Available letters:', getAvailableLetters(lettersGuessed)

        #input letter
        guessLetter = str(raw_input('Please guess a letter: '))
        guessLetter = guessLetter.lower()

        #letter already guessed
        if guessLetter in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed)
            continue

        #check letter in word
        lettersGuessed.append(guessLetter)
        if guessLetter in secretWord:
            print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
        else:
            print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
            guessLeft -= 1
        

        #check if word guessed, return if true
        if(isWordGuessed(secretWord, lettersGuessed)):
            #print separator
            print '-'*12
            print 'Congratulations, you won!'
            return True
        continue

    # guesses finished, game lost
    print '-'*12
    print 'Sorry, you ran out of guesses. The word was', secretWord + '.'
    return False

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
