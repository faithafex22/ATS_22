num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("sorry factorial does not exist for negative numbers")
elif num == 0:
    print(factorial)
else:
    for i in range (0, num + 1):
        factorial = factorial*i
    print(factorial)