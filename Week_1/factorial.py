
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("sorry factorial does not exist for negative numbers")
elif num == 0:
    print(factorial)
else:
    for i in range (1, num + 1):
        factorial = factorial*i
    print(factorial)

    import math 
n = input("Enter a number: ") 
factorial = math.factorial(int(n))
print(f"The factorial of {n} is: {factorial}") 
