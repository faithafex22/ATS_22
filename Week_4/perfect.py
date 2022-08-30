def perfect(num):
    y = []
    for i in range(1, num):
        if num % i == 0:
            y.append(i)
    x = sum(y)
    if x == num:
        print(num)
        
        
        
        
def check():      
    return[num for num in range(1, 10000) if perfect(num)]
    
check()
    



