import random 
import time

userGuesslist = []
userGuesses = []
playGame = True
continueGame = "Y"

words = ['inherit', 'computer', 'science', 'program',
         'python', 'project', 'player', 'variable',
         'reverse', 'abstract', 'polymer', 'django']

name = input("Enter your name: ")
print(f"Hello {name} welcome, let us play the hangman game! ")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time, don't forget to press 'enter key' after each guess.")
time.sleep(1)
print("Let the fun begin, I wish you a good luck!")
time.sleep(1)

while True:

    while True:
        word = random.choice(words)
        print(word)
        break
    if playGame():
        wordList = list(word)
        turn = 8

    
        def printGuessedLetter():
            print("Your Secret word is: " + ''.join(userGuesslist))


        for n in wordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("The number of allowed guesses for this word is:", turn)


        while True:

            print("Guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("You already guessed this letter, try something else.")

            else:
                turn -= 1
                userGuesses.append(letter)
                if letter in wordList:
                    print("Nice guess!")
                    if turn > 0:
                        print(f"You have {turn}  guess left!")
                    for i in range(len(wordList)):
                        if letter == wordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter
                    printGuessedLetter()

                else:
                    print("Oops! Try again.")
                    if turn > 0:
                        print(f"You have {turn} guess left!")
                    printGuessedLetter()


            joinedList = ''.join(userGuesslist)
            if joinedList == word:
                print("Yay! you won.")
                break
            elif turn == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print(f"The secret word was: {word}")
                break

        
        continueGame = input("Do you want to play again? Y to continue, any other key to quit: ")
        if continueGame == 'Y':
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("Thank You for playing. See you next time!")
            break
    else:
        break