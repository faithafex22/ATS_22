#alist = []
#for number in range(1,11):
   # alist += [number]
    #print(alist)

#for iteration
#for item in alist:
    #print(item)

#for index
#for i in range (len(alist)):
   # print(alist[i])

#values = []
#for i in range(10):
#    newvalue = int(input("Enter integer : "))  #(i+1))) 
#    values += [newvalue] 
#for i in range (len(values)):
    #print (f'{i}  {values[i]}   {"*" * values[i]}'
    
    
grades = { "John": 87, "Steve": 76, "Laura": 92, "Edwin": 89 }
#print ("\nAll grades:", grades)
grades["Steve"] = 90
#print(grades)
grades["Faith"] = 100
del(grades["John"])
#print(grades)

#playlist = []
print
#for i in range( 5 ):
    ##playlist.append( playName )
    #i = i + 1
    #print(playlist)

responses = [ 1, 2, 6, 4, 8, 5, 9, 7, 8, 10,
1, 6, 3, 8, 6, 10, 3, 8, 2, 7,
6, 5, 7, 6, 8, 6, 7, 5, 6, 6,
5, 6, 7, 5, 6, 4, 8, 6, 8, 10 ]

#print(f'{"rating":>5}    {"frequency":>13}' )
#for i in range (1, 11):
#    print(f'{i:>6} {responses.count(i):>14}')
#
#oldlist = [1, 2, 3, 4, 5]
#newlist = [6,7,8, 9, 10]
#oldlist.extend(newlist)
#print(oldlist)

#table1 = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
#table2 = ( ( 1, 2 ), ( 3, ), ( 4, 5, 6 ) )
#for item in table1[0]:
#   # print(item, end=" " )
#    continue
#for item in table1[1]:
#    print(item, end=" ")
#    #for item in row:
#       # print()


def minimum(grades):
    grades = [ [ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
    #row = student
    #column = exams = score
    lowestgrade =  100
    for i in grades:
        for j in i:
            if j < lowestgrade:
                    lowestgrade = j
    print(lowestgrade)

minimum(grades)

def maximum(grades):
    grades = [[ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
    highestgrade = 0
    for i in grades:
        for j in i:
            if j > highestgrade:
                highestgrade = j
    print(highestgrade)

maximum(grades) 

def average(grades):
    grades = [[ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
    total = 0
    for i in grades:
        for j in i:
            total = total + j
    print(total)
    n = len(grades)
    print(n)
    print (total/n)

average(grades)
     


grades = [[ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
sum = sum(grades[0])
print(sum)

          
