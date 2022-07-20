#A signup and sign-in program that take basic info:
#on signup - username, first name, lastname, password and confirm password and saves it in a csv file.
#On signin, it takes username and password and return whether a message saying login successful or invalid login credentials. 
# Add validation. Password must be minimum of 8 characters.
import csv
#signup
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

#signin
usernamec = input("Enter your username: ")
passwordc = input("Enter your password: ")
if usernamec == username and passwordc == password:
    print("login sucessful, welcome," + " " + usernamec)
if usernamec != username and passwordc != password:
    print("invalid credentials, username or password incorrect")