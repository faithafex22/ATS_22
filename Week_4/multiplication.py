#Write a program to print multiplication table of a given number till 12

def multiply (n):
    for i in range (1, 13):
        multi = n * i
        print(multi)

multiply(2)