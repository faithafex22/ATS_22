y = []
for num in range(2, 1000):
    for i in range(2, num):
        if num%i == 0:
            num = 0
            y.append(num)
            break
    else:
        num = 1
        y.append(num)
print(y, end=" ")

for index, num in enumerate(y, start=2):
    if num == 1:
        print(index, end=" ")

    

##mylist = [ v for v in range(1, 1000)]

##for k,v in enumerate(list):
    ##for character in list:
         

