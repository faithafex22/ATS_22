def perfect(num):
    y = []
    for i in range(1, num):
        if num % i == 0:
            y.append(i)
    if sum(y) == num:
        print(y)
        return num
        #print("This number is a perfect number")
    #print("This number is not a perfect number")      
#perfect(6)

def check():
    #return [num for num in range(1, 10000) if perfect(num)]
    return [num for num in range(1, 10000) if perfect(num)]
    
print(check())



