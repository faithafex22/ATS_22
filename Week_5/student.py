
def minimum():
    grades = [ [ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
    #row = student
    #column = exams = score
    lowestgrade =  100
    for i in grades:
        for j in i:
            if j < lowestgrade:
                    lowestgrade = j
    print(lowestgrade)
minimum()

def maximum():
    grades = [[ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
    highestgrade = 0
    for i in grades:
        for j in i:
            if j > highestgrade:
                highestgrade = j
    print(highestgrade)

maximum() 

def average():
    grades = [[ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
    total = 0
    for i in grades:
        for j in i:
            total = total + j
    print(total)
    n = len(grades)
    print(n)
    print (total/n)

average()
     


grades = [[ 96, 87, 89, 81 ], [ 77, 68, 86, 73 ], [ 70, 90, 86, 81 ] ]
sum = sum(grades[0])
print(sum)

          
