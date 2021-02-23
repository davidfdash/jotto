import re

word1 = input("Player 1, please enter a 5 letter word: ")
guess = ""

#is it the word? if so, you win, if not proceed
while guess != word1:
#guess a word
    guess = input("Guess a five letter word: ")
#compare letters to word1 and return number of letters in common
    c = 0
    for i in word1: 
        if re.search(i,guess): 
            c=c+1
    print(c)
 if so, you win,
else:
    print("you win!")