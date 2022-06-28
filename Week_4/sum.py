#Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
#For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

def add(n):
    sum = 0
    for i in range (0, n+1):
        i = i + 1
        sum = sum + i
        if i != n:
            continue
        print(sum)

add(10)