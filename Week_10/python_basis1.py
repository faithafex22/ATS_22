#Write a Python program to print the following string in a specific format (see the output).
#1#Sample String: "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"
#print("Twinkle, twinkle, little star\n\t\tHow I wonder what you are!\n\tup above the world so high,\nlike a diamond in the sky")
#
##2sys
#import sys
#print(sys.version)
#print(sys.version_info)
#
##3
#import datetime
#present_time = datetime.datetime.now()
#print(present_time)
#
##4
#from math import pi
#def area(radius):
#    return pi * radius**2
#
#print(area(1.1))
#5
#def rearrange():
#    fullname = []
#    firstname = input("welcome, what is your first name: ")
#    lastname = input("what is your second name: ")
#    fullname.append(firstname)
#    fullname.append(lastname)
#    print (fullname)
#    fullname.reverse()
#    return fullname
#
#print(rearrange())
#6
#user = input("hello user, please enter a sequence of comma seperated numbers: ")
#x = list(user)
#y = tuple(user)
#print(x)
#print(y)
##7
#user2 = input("hello enter the name of your file: ")
#print(user2.split(".")[1])
##8
#color_list = ["Red","Green","White" ,"Black"]
#print(color_list[0], color_list[-1])

#def comp():
#    n = input("enter an integer: ")
#    a = int(n) + int(n+n) + int(n+n+n)
#    return a
#print(comp())
#
#print(abs(5.2234))
#
#import calendar
#
#y = int(input("enter the year calender you want to print: "))
#m = int(input("enter the month calender you want to print: "))
#cal = calendar.month(y, m)
#print(cal)

#from datetime import date
#diff = date(2014, 7, 11) - date(2014, 7, 9)
#print(diff.days)
#
#from math import pi
#print(4/3 * pi * 6**3)
#
#def check(num):
#    if num < 17:
#        return 17-num
#    else:
#        return 2 * (num-17)
#print(check(22))
#
#def near():
#    n = input("enter a number to check: ")
#    a = list(n)
#    if a[0] == str(1):
#        return("This is an hundred of 1000")
#    elif a[0] == str(2):
#        return("This is an hundred of 2000")
#print(near())
#    
#letter = "alright"
#if "ls" not in letter:
#    letter = "ls" + letter
#    print(letter) 

#def larger_str(str, num):  
#    return str * num
#print(larger_str("hello", 3))
#
#user3 = int(input("welcome input a number: "))
#if user3 % 2 == 0:
#    print("Hello, you entered an even number")
#elif user3 % 2 != 0:
#    print("Hello, you entered an odd number")
#
#def large_str(str, num): 
#    if len(str) > 2:
#        str = str[:2]
#    elif len(str)<= 2:
#        str = str
#        return str * num
#print(large_str("he", 3))
#
def checker():
    vowel = ['a', 'e', 'i', 'o', 'u']
    let = input("enter an input here: ")
    if let not in vowel:
        print("this is not a vowel letter")
    else:
        print("this is a vowel letter")
checker()

def there(value, entry:list):
    if value in entry:
        return True
    else:
        return False

print(there(5, [2,3,4,5,6]))