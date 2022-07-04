def fibonacci(n):
    if n < 0:
        print ("Cannot find the fibonacci of a negative number.")
    if n == 0 or n == 1: # base case
        return n
    else:
        return fibonacci( n - 1 ) + fibonacci( n - 2)
    
print(fibonacci(10))