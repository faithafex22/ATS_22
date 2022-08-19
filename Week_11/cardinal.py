#1. Cardinal number
#2. Basic Calculator
#3. number guess game (5 trials)
#4. hangman (Uses a list (file) of words of varying length and the number of trials = length of longest word i.e 8)
#5. password generator
#6. complex numbers
#7. rational numbers
#8. create rectangle (OOP)
#9. building on rectangle formation by coordinates
#10. Tic Tac Toe

def cardinal(num):
    output =""
    if num >=4 and num <=20:
        output = str(num) + "th"
    elif num % 10 >= 4 and num% 10 <= 20:
        output = str(num) + "th" 
    elif num % 100 >= 4 and num% 100 <= 100:
        output = str(num) + "th"
    elif num == 1 or num%10 == 1:
        output = str(num) + "st"
    elif num == 2 or num%10 == 2:
        output = str(num) + "nd"
    elif num == 3 or num%10 == 3:
        output = str(num) + "rd"
    
    
    return output
    
print(cardinal(1113))
    
        
    
