from ps4a import *
import time

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print "Current Hand:",
        displayHand(hand)
        # Ask user for input
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            score = getWordScore(word, n)
            total_score += score
            print "\""+word+"\""+" earned",score,"points. Total:",total_score,"points."
            # Update the hand
            hand = updateHand(hand, word)
        # Otherwise (the word is valid):
        else:
            break
        print
    print "Total score:",total_score,"points."
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    user_input = ''
    hand = {}
    ask_user_input = True
    while user_input != 'e':
        if ask_user_input:
            user_input = raw_input("Enter n to deal a new hand, r to replay "
                                   "the last hand, or e to end game:")
        if user_input == 'n':
            user_or_comp = raw_input("Enter u to have yourself play, c to "
                                     "have the computer play:")
            if user_or_comp == 'u':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
                ask_user_input = True
            elif user_or_comp == 'c':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
                ask_user_input = True
            else:
                print "Invalid command."
                ask_user_input = False
        elif user_input == 'r':
            if not hand:
                print "You have not played a hand yet. Please play a new " \
                      "hand first!"
                print
                continue
            else:
                user_or_comp = raw_input("Enter u to have yourself play, c to "
                                     "have the computer play:")
                if user_or_comp == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif user_or_comp == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print "Invalid command."
        elif user_input != 'e':
            print "Invalid command."
        print

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    #print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    #print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    #print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)
    #compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    playGame(wordList)


