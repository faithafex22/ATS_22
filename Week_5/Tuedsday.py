#5.3
num = []
for i in range(20):
    x = int(input("Enter your number here: "))
    if x not in num:
       num.append(x)
    print(num)

#5.8
#from random import randint
#from collections import Counter
#mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
#x, y = 1, 99
#mydict = dict()
#for ele in mylist:
#    mydict[ele] = randint(x,y)
#print(mydict)

#count = Counter(mydict.values())
#print(count)

#print([2000 + item  for item in range(0, 21)])
#5.8
import random
from collections import Counter
randomlist = []
mydict = {}
duplicatelist = []

for i in range(1, 21):
    n = random.randint(1, 100)
    print(n, end=" , ")
    randomlist.append(n)
print(randomlist)
c = Counter(randomlist)
for k in c: 
    if c[k] > 1:
        duplicatelist.append(k)
print("there is duplicate")
print(duplicatelist)
for ele in randomlist:
    mydict[str(ele)] = ele
print(mydict)

#5.5
Primes = [0] * 500001
def SieveOfEratosthenes(n) :
    Primes[0] = 1
    i = 3
    while(i*i <= n) :
        if (Primes[i // 2] == 0) :
            for j in range(3 * i, n+1, 2 * i) :
                Primes[j // 2] = 1
                 
        i += 2
        
if __name__ == "__main__":
 
    n = 1000
    SieveOfEratosthenes(n)
    for i in range(1, n+1) :
        if (i == 2) :
            print( i, end = " ")
        elif (i % 2 == 1 and Primes[i // 2] == 0) :
            print( i, end = " ")


#5.6 
def bubblesort(oldlist):

    swapped = False
    for i in range(len(oldlist)-1):
        for j in range(0, len(oldlist)-i-1):
            if oldlist[j] > oldlist[j+1]:
                swapped = True
                oldlist[j], oldlist[j+1] = oldlist[j+1], oldlist[j]
        if not swapped:
            return 

    
oldlist=[9, 4, 6, 10 , 50, 30, 96, 88, 40, 72]
bubblesort(oldlist) 
print(oldlist)    

#5.7
def binarySearch(array, searchelement, low, high):
    if high >= low:
    
        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == searchelement:
            return mid

        # Search the left half
        elif array[mid] > searchelement:
            return binarySearch(array, searchelement, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, searchelement, mid + 1, high)

    else:
        return -1


array = [4, 8, 10, 12, 15, 17, 18]
searchelement = 12
result = binarySearch(array, searchelement, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


#5.4

salesperson = [{'sp1':400, 'sp2':300, 'sp3':500, 'sp4':1000},
            {'sp1':500, 'sp2':600, 'sp3':700, 'sp4':200},
            {'sp1':800, 'sp2':1000, 'sp3':400, 'sp4':900}, 
            {'sp1':750, 'sp2':850, 'sp3':950, 'sp4':650},
            {'sp1':600, 'sp2':700, 'sp3':850,  'sp4':250}]
    
salespersonlist = []

salesperson1 = sum(item['sp1'] for item in salesperson)
salespersonlist.append(salesperson1)
salesperson2 =sum(item['sp2'] for item in salesperson)
salespersonlist.append(salesperson2)
salesperson3 = sum(item['sp3'] for item in salesperson)
salespersonlist.append(salesperson3)
salesperson4 = sum(item['sp4'] for item in salesperson)
salespersonlist.append(salesperson4)
print(salespersonlist)

sum1 = 0 
for i in salespersonlist:
    sum1 = sum1 + i
    i = i + 1
print(sum1)
totalsalesbysalesperson = sum1

products = [{'pd1':400, 'pd2':500, 'pd3':800, 'pd4':750, 'pd5':600},
            {'pd1':300, 'pd2':600, 'pd3':1000, 'pd4':850, 'pd5':700},
            {'pd1':500, 'pd2':700, 'pd3':400, 'pd4':650 , 'pd5': 850}, 
            {'pd1':1000, 'pd2':200, 'pd3':900, 'pd4':950, 'pd5':250}]
            

productlist = []

product1 = sum(item['pd1'] for item in products)
productlist.append(product1)
product2 =sum(item['pd2'] for item in products)
productlist.append(product2)
product3 = sum(item['pd3'] for item in products)
productlist.append(product3)
product4 = sum(item['pd4'] for item in products)
productlist.append(product4)
product5 = sum(item['pd5'] for item in products)
productlist.append(product5)
print(productlist)

sum2 = 0
for i in productlist:
    sum2 = sum2 + i
    i = i + 1
print(sum2)
salesbyproduct = sum2
import tabulate
salestable = [["", "salesperson1", "salesperson2", "salesperson3", "salesperson4", "totalsalesperprod"]
   ["product1", 400, 300, 500, 1000, 2200]
   ["product2", 500, 600, 700, 200, 2000]
   ["product3", 800, 1000, 400, 900, 3100]
   ["product4", 750, 850, 950, 650, 3200]
   ["product5", 600, 700, 850, 250, 2400]
   ["totalsalespersalesperson", 3050, 3450, 3400, 3000]]
print(tabulate.tabulate())
























        
    










