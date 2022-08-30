import pprint
from datetime import date


people = [{"f_name":"Faith", "l_name":"Adeosun", "day_month": "1st of January", "attendance": 30, "height": 126, "weight": 60, "age": 25},
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
   
#fuction to increament attendance of a particular profile
def increment(firstname:str):
     for i in people:
        if i["f_name"] == firstname:
            i["attendance"] = i["attendance"] + 1
            newattendance = i["attendance"]
            return f"{firstname}, your new attendance is {newattendance}"
print(increment("Faith"))

#function to update the name of a particular profile
def update(firstname, new_fname, new_lname):
     for i in people:
        i["f_name"] = new_fname 
        i ["l_name"] = new_lname
        return f"{firstname}, your new name is {new_fname} {new_lname}"
print(update("Faith", "Esther", "Akande"))

#function to update a fullname into title case
def make_title(first_name, last_name):
     return f"{first_name} {last_name}".title()
print(make_title("awwal", "adeleke"))

#function to return all fullname in titlecase
def titlecase():
    names_list = []
    for i in people:
        firstname = i["f_name"] 
        lastname = i["l_name"]
        names_list.append(f"{firstname} {lastname}".title())
    return names_list
print(titlecase())

#function that add new profile
def addprofile(firstname, lastname, dateofbirth, attendance, height, weight, age):
        newperson = {'f_name': firstname, 'l_name': lastname, 'day_month': dateofbirth, 'attendance': attendance,
                      'height': height, 'weight': weight, 'age': age}  
        print(f"A new student is just added, {firstname} {lastname} by name")
        people.append(newperson)
        return people
print(addprofile("Joy", "Gladys", "9th of November", 30, 135, 70, 26))

#function that get number of students in the list
def countstudents():
    return len(people)
print(countstudents())

#function that remove a profile
def removeprofile(name):
    for i in people:
        if i["f_name"] == name:
            people.remove(i)
            break
    return people   
pprint.pprint(removeprofile("Adebusola"))
 
#function that gets the birth month of a particular profile
def getbirthmonth(myname):
    for i in people:
        if i["f_name"] == myname:
            dob = i["day_month"]
            dob = (dob.split(" ")[2])
            return(f"{myname}, your birthmonth is {dob}")
print(getbirthmonth("Awwal"))
 
#function to return list of initials
def initials():
    mylist = []
    for i in people: 
            firstname = i["f_name"]
            lastname = i["l_name"]
            nameinitials = f"{firstname[0:1]} . {lastname[0:1]}"
            mylist.append(nameinitials)
    return mylist
print(initials())
 
#function that returns BMI of a profile
def calculate_BMI(name):
    for i in people:
        if i["f_name"] == name:
         BMI = i["weight"]/(i["height"]/100)**2
         return (f"BMI of {name} is {round(BMI)}")
print(calculate_BMI(name="Abraham"))

#function that returns minimum age of the class
def min_age():
    mini_age = people[0]["age"]
    for i in people:
        current_age = i["age"]
        if current_age < mini_age:
            mini_age = current_age
    return(f"Minimum age is {mini_age}")
print(min_age())

#function that returns maximum age
def max_age():
    maxi_age = people[0]["age"]
    for i in people:
        current_age = i["age"]
        if current_age > maxi_age:
            maxi_age = current_age
    return(f"Maximum age is {maxi_age}") 
print(max_age())

#function that return the average of ages of students in clas
def average():
        sum_ages = 0
        for i in people:
            sum_ages = sum_ages + i["age"]
            n = len(people)
            avearage = sum_ages/n
        return round (avearage) 
print(average())

#function that calculates birth year
def birth_year(firstname):
    for i in people:
        if firstname == i["f_name"]:
            yearofbirth = date.today().year - i["age"]
    return f"The year that {firstname} was born is {yearofbirth}"
print(birth_year(firstname="Esther"))

#function to group students according to their birth months
def get_one(i):
   month_dict = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December" }
   profile_month = i["day_month"].split()[2]
   month_num = [k for k, v in month_dict.items() if v == profile_month]
   return month_num
def group_profiles():
   people.sort(key=get_one)
   pprint.pprint(people)

group_profiles()

