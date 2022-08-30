
num = int(input("Enter number: "))
rev = 0 
y = num
while (num>0):
    dig = num%10
    rev = rev*10+dig
    num = num//10
if(y==rev):
    print('The number is a palindrome')
else:
    print('The number is not a palindrome')
