import random
import string

# choose direction of words.txt file, which you can download
WORDLIST_FILENAME = "D:/Docs/Coding/MOOC/6.00x/Exercises/MIT-6.00x.git/Problem Set 3/words.txt"

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
    if secretWord == '':
        return True
    if secretWord[0] in lettersGuessed:
        return isWordGuessed(secretWord[1:], lettersGuessed)
    return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ['_ '] * len(secretWord)
    letterIndex = 0
    output = ''
    n = 0
    for letter in secretWord:
        s = secretWord[n:]
        letterIndex = n
        if s[0] in lettersGuessed:
            result[letterIndex] = letter + ' '
        n += 1
    for i in result:
        output += i
    return output

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lettersList = []
    output = ''
    for i in letters:
        lettersList.append(i)
    nextList = lettersList[:]
    for i in nextList:
        if i in lettersGuessed:
            lettersList.remove(i)
    for i in lettersList:
        output += i
    return output
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    '''
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    mistakesMade = 0
    while True:
        numberGuesses = 8
        availableLetters = getAvailableLetters(lettersGuessed)
        print '------------'
        print 'You have', numberGuesses - mistakesMade, 'guesses left.'
        print 'Available letters:', availableLetters
        guess = raw_input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        lettersGuessed.append(guessInLowerCase)
        wordSoFar = getGuessedWord(secretWord, lettersGuessed)
        win = isWordGuessed(secretWord, lettersGuessed)
        if guessInLowerCase not in availableLetters:
            print "Oops! You've already guessed that letter:", wordSoFar
        elif guessInLowerCase in secretWord:
            print 'Good guess:', wordSoFar
        elif guessInLowerCase not in secretWord:
            mistakesMade += 1
            print 'Oops! That letter is not in my word:', wordSoFar
        if win:
            print '------------'
            print 'Congratulations, you won!'
            break 
        if numberGuesses - mistakesMade == 0:
            print '------------'
            print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) +'.'        
            break

# Random test
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)