def prime(num):
    a=[]
    for i in range (1, num+1):
        if (num/i).is_integer():
            a.append(i)
    if len(a)==2:
        print("Prime")
    else:
        print("Not Prime")




n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n//2):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is neither prime nor composite")