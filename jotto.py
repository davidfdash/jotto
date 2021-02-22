import re

word1 = input("Player 1, please enter a 5 letter word: ")
guess = ""
#guess a word
#is it the word? if so, you win, if not proceed
while guess != word1:
    guess = input("Guess a five letter word: ")
    c = 0
    for i in word1: 
        if re.search(i,guess): 
            c=c+1
    print(c)
else:
    print("you win!")
#compare letters to word1 and return number of letters in common

#repeat until it is the word