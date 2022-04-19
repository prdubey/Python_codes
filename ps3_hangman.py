# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    # FILL IN YOUR CODE HERE...
    cnt = 0
    for l in secretWord :
        for lg in list(set(lettersGuessed)):
            if l == lg:
                cnt +=1
    return cnt == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    gw = list(len(secretWord)*"_")
    sw_copy = list(secretWord[:])
    for l in list(set(lettersGuessed)):
        for lg in secretWord:
            if l == lg:
                indx = sw_copy.index(lg)
                gw[indx] = lg
                sw_copy[indx] = '_'
    return ''.join(gw)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabets =list('abcdefghijklmnopqrstuvwxyz')
    alph_copy = alphabets[:]
    for l in alphabets:
        if l in set(lettersGuessed):
            alph_copy.remove(l)
    return ''.join(alph_copy)
    

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord)," letters long.")
    unknown_wrd = len(secretWord)*"_"
    print(12*"_")
    print("You have 8 guesses left.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    cnt = 0
    guess_lst = []
    alphabets =list('abcdefghijklmnopqrstuvwxyz')
    while cnt <= 8:
        guess = (input("Please guess a letter:"))
        if guess not in alphabets:
            print("Oops! You've already guessed that letter:", unknown_wrd)
        else:
            guess_lst.append(guess)
            part_wrd = (getGuessedWord(secretWord, guess))
            if part_wrd == unknown_wrd:
                print("Oops! That letter is not in my word:",part_wrd)
                print(12*"_")
                cnt += 1
                print("You have ", 8 - cnt," guesses left.")
                alphabets = getAvailableLetters(guess_lst)
                print("Available letters: ",alphabets)
                unknown_wrd = part_wrd
            else:
                print("Good guess: ",part_wrd)
                print(12*"_")
                unknown_wrd = part_wrd
                print("You have ", 8 - cnt," guesses left.")
                alphabets = getAvailableLetters(guess_lst)
                print("Available letters: ",alphabets)
                unknown_wrd = part_wrd
           
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
