print "Please think of a number between 0 and 100!"
min = 0
max = 100
guess = max/2
print "Is your secret number", str(guess)+"?"
ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to "
                "indicate the guess is too low. Enter 'c' to indicate I "
                "guessed correctly.")
while ans != 'c':
    if ans == 'h':
        #Guess is high
        max = guess
        guess = (guess + min) / 2
    elif ans == 'l':
        #Guess is low
        min = guess
        guess = (guess + max) / 2
    elif ans != 'c':
        print "Sorry, I did not understand your input."
    print "Is your secret number", guess,"?"
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to "
                "indicate the guess is too low. Enter 'c' to indicate I "
                "guessed correctly.")
print "Game over. Your secret number was:", guess