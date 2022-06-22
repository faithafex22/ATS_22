#Write a program that asks the user to enter 5 numbers, save the numbers in a list and print the listdef  book(list:int):
output = (input("Enter any five numbers of your choice:"))
formal = list(output)



def book(numlist):
    sum = 0
    for i in range (0, len(numlist)):
        n = len(numlist)
        sum = sum + (int(numlist[i]))
        average = sum/n
    return average;
print(book(formal)) 

#note you cant convert a  whole list into an integer at once, you have to loop through each element in it.