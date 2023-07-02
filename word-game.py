
# Word Guessing Game Assignment with random word selection
# 11/1/22
import random
# variables for random word
words = ["fashion", "careful", "faculty", "friends", "journey",
         "healthy", "quickly", "jumping", "quality", "amplify",
         "voyager", "angrily", "strange", "working", "anxious",
         "kitchen", "upgrade", "imagine", "liberty", "picture"]
word = words[random.randint(0, 19)]
length = len(word)
list = []
counter = 0
# guessing game code
print("Welcome to the word guesssing game!")
print("You will be given 10 attempts to guess the word.")
print("The word has 7 letters")
print(*list)
counter = 0
while counter < length:
    list.append("-")
    counter = counter + 1
    print(*list)
    counter = 0
while (counter < 10):
    counter = counter + 1
    letter = input("Guess a letter/word: ")
    foundit = word.find(letter)
    # ends game if you guess the word at once
if letter == word:
    print("You guessed the word!")
    counter = counter + 1

#prints letter if it is less than 0
elif foundit >= 0:
    list.pop(foundit)
    list.insert(foundit, letter)
    print("guessed correctly")
    print(*list)
    # does not print letter if it is less than 0
elif foundit < 0:
    print("guessed incorrectly")
    print(*list)
    # ends game if you guess the word letter for letter
if "-" not in list:
    print("you guessed all the letters")
    
