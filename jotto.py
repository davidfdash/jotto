from collections import Counter

word1 = input("Player 1, please enter a 5 letter word: ")
guess = ""
#guess a word

while guess != word1:
    guess = input("Guess a five letter word: ")
    dict1 = Counter(word1)
    dict2 = Counter(guess)
    commonDict = dict1 & dict2
    commonCharacters = list(commonDict.elements())
    
#is it the word? if so, you win, if not proceed

#compare letters to word1 and return number of letters in common

#repeat until it is the word