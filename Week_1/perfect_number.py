# Python program to check perfect number using function

def perfect_numbers(N):  #user-defined function
   sum = 0
   for i in range(1,N): 
      if(N%i == 0):
         sum = sum+i 
   return sum 

# take inputs
N = int(input("Enter a number: "))

# check perfect number or not
if(N == perfect_numbers(N)): 
   print(N, "is a perfect number") 
else: 
   print(N, "is not a perfect number") 


n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")