print "Please think of a number between 0 an 100!"

def GuessNumber(high):
    low = 0
    guess = (high + low) / 2
    answer = ''
    while answer != 'c':
        print 'Is your secret number ' + str(guess) + '?'
        print "Enter 'h' to indicate the guess is too high.",
        print "Enter 'l' to indicate the guess is too low. ",
        print "Enter 'c' to indicate I guessed correctly."
        answer = raw_input()
        if answer == 'l':
            low = guess
        elif answer == 'h':
            high = guess
        else:
            print "Sorry, I did not understand your input."
        guess = (high + low) / 2
    print "Game over. Your secret number was " + str(guess)
print GuessNumber(150)