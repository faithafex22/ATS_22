#4. Modify (3) 
#a. After successful signup, it should prompt the user to signin
#b. After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
#c. Edit profile should ask for more information like phone_number (required), address (optional), date of birth (optional) and gender (compulsory)

import csv
from this import d
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
username = firstname + " " + lastname
password = input("Enter your password: ")
confirm_password = input("confirm your password: ")

if password.isalnum == False:
    print("password must contain both numbers and letters")
if len(password) < 8:
    print("password must at least be 8 characters: ")
if password != confirm_password:
    print("The password you entered does not match")

fieldnames = ["firstname", "lastname", "username", "password", "confirm_password"]
row = {
    "firstname":firstname, "lastname":lastname, "username":username, "password":password, "confirm_password": confirm_password 
}

with open("bio.csv", "w", encoding="utf8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(row)

print("you have successfully sign up, you can now sign in")
username = input("Enter your username: ")
password = input("Enter your password: ")
print("welcome" + " " + username + " "  + "you can edit your profile, change your password or logout")

A = input("type x to edit your profile, y to change password or z to logout: ")
B = ["x", "y", "z"]
C = []
D = ["firstname", "lastname", "username", "password", "confirm_password", "phoneno", "address", "dateofbirth", "gender"]
for i in B:
    if i == "x" == A:
        print("you can now edit your profile")
        phonenum = int(input("Enter your phonenumber: "))
        print("this feed is required")
        address = input("Enter your address: ")
        print("This feed is optional")
        dateofbirth = input("Enter your date of birth, it should be in this format DDMMYYYY: ")
        print("This feed is optional")
        gender = input("Enter your gender: ")
        print("This feed is required")
        C.append([firstname, lastname, username, password, confirm_password, phonenum, address, dateofbirth, gender,])
        #print(C)

    if i == "y" == A:
        print("you can now change your password ")
        new_password = input("Enter 8 characters, it must contain both numbers and letters: ")
        input("confirm your new password: ")
        password = new_password
        confirm_password = new_password
        print("you have successfully changed your password")
        fieldnames = ["firstname", "lastname", "username", "password", "confirm_password"]
        row = {
        "firstname":firstname, "lastname":lastname, "username":username, "password":password, "confirm_password": confirm_password 
         }

    if i == "z" == A:
        print("to logout, simply click on the logout button\n you are logged out!")

with open ("bio.csv", "w", encoding="utf8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(row)




