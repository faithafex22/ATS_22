def avetotal():
    gallons = []
    miles = []
    while True:
        m = float(input("Enter the number 0f miles driven: "))
        g = float(input("Enter the amount of gallons used: "))
        if m == -1 or g == -1:
            print("This is not possible")
            break
        print(f"The miles per gallon for this tank was {m/g}")
        miles.append(m) 
        gallons.append(g)
        
        
    average = sum(miles)/sum(gallons) 
    print(f"The overall aaverage miles/garlons was {average}")
        
    
avetotal() 

