low = 0
high = 100
number = 0
ans = (high + low) / 2
print "Please think of a number between 0 an 100!"
while True:
    print 'Is your secret number ' + str(ans) + '?'
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. ",
    print "Enter 'c' to indicate I guessed correctly.",
    number = raw_input()
    if number == 'l':
        low = ans
    elif number == 'h':
        high = ans
    elif number == 'c':
        print "Game over. Your secret number was " + str(ans)
        break
    else:
        print "Sorry, I did not understand your input."
    ans = (high + low) / 2    