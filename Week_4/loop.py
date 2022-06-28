#using continue
#Write a for loop that prints out numbers from 1 to 10
for i in range (1, 11):
    if i == 4:
        continue
    print(i,  end = ", ")
	
#Write a for loop that prints out even numbers between 1 and 1000
for i in range (1, 1001):
    if i % 2 != 0:
        continue
    print(i, end = ", ")

#write a for loop that prints out odd numbers between 1 and 1000
for i in range (1, 1001):
    if i % 2 == 0:
        continue
    print(i, end = ", ")
        
#Write a while loop equivalent for the tasks above

i = 1
while i < 11:
    i = i + 1
    if i == 4:
        continue
    print(i, end = ", ")


i = 1
while i < 1001:
    i = i + 1
    if i % 2 != 0:
        continue
    print(i, end = ", ")
    

i = 1
while i < 1001:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i, end = ", ")
    
