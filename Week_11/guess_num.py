from random import randint
def guessnum():
    mydigit= randint(1, 1000)
    print(mydigit)
    print("\nI have a number between 1 and 1000. \nCan you guess my number? ")
    for i in range(5):
        x = int(input("Please enter your  guessed number: "))
        if x == mydigit:
            print("\nExcellent! You guessed the number! \nWould you like to play again (y or n): ")
            z = input()
            if z == "y":
                guessnum()
            if z == "n":
                exit()
            break
        if x < mydigit:
            print("Number is too low, try again.")
        if x > mydigit:
             print("Number is too high, try again.")
    print("you have exceeded your numbers of tries")
            
        

guessnum()
    