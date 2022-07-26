from datetime import date
people =[{"f_name":"Faith", "l_name":"Adeosun", "day_month": "1st of January", "attendance": 30, "height": 126, "weight": 60, "age": 25},
         {"f_name":"Toluwanimi", "l_name":"Ogunbiyi", "day_month": "2nd of May", "attendance": 30, "height":137 , "weight": 50, "age": 25},
         {"f_name":"Lukman", "l_name":"Abisoye", "day_month": "3rd of October", "attendance": 30, "height": 118, "weight": 60, "age": 24},
         {"f_name":"Ahmad", "l_name":"Sarafudeen", "day_month": "4th of July", "attendance": 30, "height": 129, "weight": 80, "age": 24},
         {"f_name":"Abdullaih", "l_name":"Salam", "day_month": "5th of June", "attendance": 30, "height": 110, "weight": 70, "age": 25},
         {"f_name":"Basheer", "l_name":"Balogun", "day_month": "6th of November", "attendance": 30, "height": 131, "weight": 70, "age": 26},
         {"f_name":"Adebusola", "l_name":"Adeyeye", "day_month": "7th of August", "attendance": 30, "height": 122, "weight": 60, "age": 27},
         {"f_name":"Awwal", "l_name":"Adeleke", "day_month": "8th of December", "attendance": 30, "height": 146,  "weight": 80, "age": 26},
         {"f_name":"Tajudeen", "l_name":"Abdullai", "day_month": "9th of September", "attendance": 30, "height": 137, "weight": 60, "age": 25},
         {"f_name":"Abraham", "l_name":"Adekunle", "day_month": "15th of May", "attendance": 30, "height": 138, "weight": 70, "age": 26},
         {"f_name":"Yusuf", "l_name":"Oyedele", "day_month": "13th of March", "attendance": 30, "height": 140, "weight": 60, "age": 27}]


class Student:
    def __init__(self, firstname) -> None:
        for i in range(len(people)):
            if firstname == people[i]['f_name']:
                self.firstname = people[i]["f_name"]
                self.lastname = people[i]["l_name"]
                self.dateofbirth = people[i]["day_month"]
                self.attendance = people[i]["attendance"]
                self.height = people[i]["height"]
                self.weight = people[i]["weight"]
                self.age = people[i]["age"]
                break
    
#method that increament attendance of a particular profile
    def increament(self):
        self.attendance = self.attendance + 1
        return f"your new attendance is now {self.attendance}"

#method that update first and lastname
    def update(self,f_name, l_name):
        self.firstname = f_name
        self.lastname = l_name
        return f"your new name is now {self.firstname} {self.lastname}"

#method that returns name in titlecase
    def fullname(self):
        return f"{self.firstname} {self.lastname}".title()

#method that add profile to list of dictionary
    def addprofile(  firstname, lastname, dateofbirth, attendance, height, weight, age):
        newperson = {'f_name': firstname, 'l_name': lastname, 'day_month': dateofbirth, 'attendance': attendance,
                     'height': height, 'weight': weight, 'age': age}  
        #print(f"A new student is just added, {self.firstname} {self.lastname} by name")
        people.append(newperson)
        return people

    print(addprofile( "Joy", "Gladys", "9th of November", 30, 135, 70, 26))

#method that get numbers of items in the list
    def getclassnum(self):
        return f"There are {len(people)} students in class"

    #print(getclassnum(people))

#method  that remove a profile
    def removeprofile(self ):
        del(people[11])
        return people

    #def removeprofile(self, name):
    #    if self.firstname == name:
    #        people.remove(name)
    #        return people   
#pprint.pprint(removeprofile("Adebusola"))

#method that gets the birth month of a particular profile
    def getbirthmonth(self):
        dob = self.dateofbirth
        dob = (dob.split(" ")[2])
        return(dob)

#method that returns a list of initials
    def listinitials(self): 
      return(f"{self.firstname[0:1]}.{self.lastname[0:1]}")
    
#method that returns BMI of a profile
    def calculate_BMI(self):
        BMI = self.weight/(self.height/100)**2
        return round(BMI)

#method that returns minimum age of the class
    #def min_age(self):
    #    mini_age = people[0]["age"]
    #    current_age = self.age
    #    if current_age < mini_age:
    #        mini_age = current_age
    #    return(f"Minimum age is {mini_age}")

#method that returns minimum age of the class
    def min_age(self):
        mini_age = people[0]["age"]
        for i in range(len(people)):
            current_age = people[i]["age"]
            if current_age < mini_age:
                mini_age = current_age
        return(f"Minimum age is {mini_age}")

##method that returns maximum age
#    def max_age(self):
#        maxi_age = people[0]["age"]
#        current_age = self.age
#        if current_age > maxi_age:
#            maxi_age = current_age
#        return(f"Maximum age is {maxi_age}") 

#methos that returns maximum age
    def max_age(self):
        maxi_age = people[0]["age"]
        for i in range(len(people)):
            current_age = people[i]["age"]
            if current_age > maxi_age:
                maxi_age = current_age
        return(f"Maximum age is {maxi_age}")

#method that returns average age of the class
    def average(self):
        sum_ages = 0
        for i in range(len(people)):
            sum_ages = sum_ages + self.age
        n = len(people)
        avearage = sum_ages/n
        return avearage 

#method that calculates birth year
    def birth_year(self):
        yearofbirth = date.today().year - self.age
        return f"The year that {self.firstname} was born is {yearofbirth}"




student1 = Student("Faith")
student12 = Student("Joy")
print(student1.increament())
print(student1.update("Esther", "Akande"))
print(student1.fullname())
print(student1.getclassnum())
print(student1.getbirthmonth())
print(student1.removeprofile())
print(student1.listinitials())
print(student1.calculate_BMI()) 
print(student1.min_age()) 
print(student1.max_age())
print(student1.average())
print(student1.birth_year())
      



 



        


