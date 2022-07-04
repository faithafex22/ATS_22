import random
def guessnum():
    mydigit= random.randrange(1,1000)
    print(mydigit)
    print("\nI have a number between 1 and 1000. \nCan you guess my number? ")
    while True:
        x = int(input("Please enter your  guessed number: "))
        if x == mydigit:
            print("\nExcellent! You guessed the number! \nWould you like to play again (y or n): ")
            z = input()
            if z == "y":
                guessnum()
            if z == "n":
                exit()
            break
        i = 0
        if i >= 5:
            print("You have exceeded your chances, you are out of the game")
            break
        if x < mydigit:
            print("Number is too low, try again.")
        if x > mydigit:
            print("Number is too high, try again.")
        i == i + 1
            
            
        
guessnum()
    
