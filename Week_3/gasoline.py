def avetotal():

    gallons = []
    miles = []
    while True:
        m = float(input("Enter the number 0f miles driven: "))
        g = float(input("Enter the amount of gallons used: "))
        if m == 1 and g == -1:
            print ("not possible")
            break
        miles.append(m) 
        gallons.append(g)
        print(miles)
        print(gallons)
        average = sum(miles)/sum(gallons) 
        print(average)
        
    
avetotal() 

