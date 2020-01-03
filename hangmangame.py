#creates a list of possible words
words=["hello","cameron","python","hangman"]
#imports  the random function for python
import random
#lets the computer pick a random word from the list
secretword=random.choice(words)
#set dashes to be the same length as whatever word is randomly selected
dash="_" * len(secretword)
#gives the user 10 tries to guess a word
guessesleft=10
#ask user to guess a word
def get_guess():
    #going to keep asking until out of guesses
    while True:
        guess=input("Guess: ")
        #if the guess is more than one letter it wont work
        if len(guess)!=1:
            print "Your guess must have one letter!"
        #if guess is uppercase it wont work
        elif not guess.islower():
            print "Your guess must be a lowercase letter!"
        else:
            return guess
#dashes function
def update_dashes(word, dashes, guess):
    #for the length of the word
    for i in range(len(word)):
        #replace the dash with whatever letter is in the word
        if word[i]==guess:
            dashes=dashes[:i]+guess+dashes[i+1:]
    return dashes
#if you still have guesses left and the dashes arent equal to the word
while guessesleft>0 and dash!=secretword:
    #print the remaining dashes and letters of the word
    print dash
    print str(guessesleft)+" guesses left."
#store guesses and update dash
    guess=get_guess()
    dash=update_dashes(secretword, dash, guess)
    if guess in secretword:
        print "Good Job! Guess again"
    else:
        print "Wrong! Pick again"
        guessesleft=guessesleft-1
#win or lose
if guessesleft==0:
    print "You lose. :( The word was: "+secretword
else:
    print "You win! :) The word was: "+secretword
