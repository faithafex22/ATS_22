number = [3, 2, 8, 5, 10, 6]
largest_number = max(number)

print("The largest number is:", largest_number)

square = {2: 4, 5: 9, -1: 1, -2: 10}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2

# the key whose value is the largest
key2 = max(square, key = lambda key: square[key])

print("The key with the largest value:", key2)    # -3

# getting the largest value
print("The largest value:", square[key2])    # 9

#names = ["Rishikesh", "aman", "Ajay", "Hemkesh", "sandeep", "Darshan", "Virendra", "Shwetabh"]
#names2 = sorted(names)
#print(names2)
#['Ajay', 'Darshan', 'Hemkesh', 'Rishikesh', 'Shwetabh', 'Virendra', 'aman', 'sandeep']
#>>> # But I don't want this o/p(here our intention is to treat 'a' same as 'A')
#...
#>>> names3 = sorted(names, key=lambda name:name.lower())
#>>> names3
#['Ajay', 'aman', 'Darshan', 'Hemkesh', 'Rishikesh', 'sandeep', 'Shwetabh', 'Virendra']
#
## find largest item in the string
#print(max("")) 
#
## find largest item in the list
#print(max([2, 1, 4, 3])) 
#
## find largest item in the tuple
#print(max(("one", "two", "three"))) 
#'two'
#
## find largest item in the dict
#print(max({1: "one", 2: "two", 3: "three"})) 
#3
#
