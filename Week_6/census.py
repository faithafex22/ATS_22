#Census program that stores firstname, lastname, middle name, age, gender, dob, occupation, marital status, email
#a. validates input
#b. saves in a csv file
#c. Ability to search by taking a search term and return matches
import csv

#def census():
#    firstname = input("Enter your firstname: ")
#    lastname = input("Enter your lastname: ")
#    middlename = input("Enter your middlename: ")
#    age = (input("Enter your age: "))
#    gender = input("Enter your gender: ")
#    dateofbirth = (input("Enter your date of birth: "))
#    occupation = input("Enter your occupation: ")
#    maritalstatus = input("Enter your maritalstatus: ")
#    email = input("Enter your email: ")
#
#    if age.isdigit() != True:
#        print('you entered a wrong input!')
#    if gender != "Male" or  gender != "Female":
#        print("input can only be Male or Female")
#    if dateofbirth.isnumeric() != True:
#        print("dateofbirth must be in this format DDMMYYYY")
#    if ".com" not in email and  email.isalnum() != True:
#        print("invalid input")
#
fieldnames = ['firstname', 'lastname', 'middlename', 'age', 'gender', 
                'dateofbirth', 'occupation' ,'maritalstatus', 'email']

#row = {"firstname": firstname, "lastname": lastname, "middlename": middlename, "age": age, 
            #"gender": gender, "dateofbirth": dateofbirth, "occupation": occupation,
            #  "maritalstatus": maritalstatus, "email": email}
#print(row)

    #with open("data.csv", "a", encoding="utf8", newline="") as f:
        #writer =  csv.DictWriter(f, fieldnames=fieldnames) 
        #writer.writeheader()
       # writer.writerow(row)

#search by fullname
    #fullname = row["firstname"] + " " + row["middlename"] + " "  + row["lastname"]
    #print (fullname)

with open("data.csv", "r", encoding="utf8", newline="")as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        #if line["firstname"] == "Bright" and line["lastname"] == "Judge":
        print(line)

