from random import randint
import sys
answer = randint(int(sys.argv[1], int(sys.argv[2])))
#print(answer)

while True:
    try:
        guess_num = int(input("Enter the no you want to guess: "))
        if 0 < (guess_num)  < 11:
            if answer  == guess_num:
                print("gotten, you are a genius")
                break
            else:
                print(" you are almost there, try again")
        else:
            print("you should only enter a number between 1 and 10")
    except ValueError:
                    print("please enter a number")
                    continue
    
