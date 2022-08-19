mylist = {num**2 for num in range (0, 100)}

print (mylist)

simple_dict = {'a': 1, "b": 2,"c": 3}

mylist = {k:v**2 for k,v in simple_dict.items() if v%2 != 0}
print(mylist)

u_list = {num:num**2 for num in [4,5,6]}

duplicates = ["a", 'b', 'c', 'c', 'b', 'e', 'f', 'g', 'h']

mylist = list(set([x for x in duplicates if duplicates.count(x)>1]))
print(mylist)

import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.strftime(("%A")))