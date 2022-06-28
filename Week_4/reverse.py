#Print list in reverse order using a loop
def change():   
    list1 = [10, 20, 30, 40, 50]
    newlist = []
    for i in reversed(list1):
        newlist.append(i)
    print(newlist)

change()