def prime(num):
    a=[]
    for i in range (1, num+1):
        if num%i == 0:
            a.append(i)
    if len(a)==2:
        print(num, end=" ")
#i = i + 1    
        #print('This is a prime number')
    #else:
        #print('This is not a prime number')
#prime(10)


def check():
    return [num for num in range(1, 1000) if prime(num)]

print(check())
#
#import math
#def prime(num):
#    if math.sqrt(num) == float and num % 2 != 0:
#    #if num % 2 != 0:
#        print("This is a prime number")
#    else:
#        print("This is not a prime number")
#
#prime(23)
    