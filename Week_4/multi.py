import random
def multi():
    digit1 = random.randrange(1,10)
    digit2 = random.randrange(1,10)
    z = digit1 * digit2
    while True:
        x = input(str(f"How much is {digit1} times {digit2}?: "))
        y = int(x)
        if y == z:
            print("very good!")
            break
        else:
            print("No, please try again.")
        
        
multi()


