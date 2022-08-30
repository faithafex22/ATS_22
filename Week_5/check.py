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
print(c)
for k in c: 
    if c[k] > 1:
        duplicatelist.append(k)
print("there is duplicate")
print(duplicatelist)
for ele in randomlist:
    mydict[str(ele)] = ele
print(mydict)

