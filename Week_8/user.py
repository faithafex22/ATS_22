class user:
    othername = "ATS" #class variable
    #def__init__ is a constructor
    def __init__(self, firstname, lastname, username, email, password):
    #instance variables 
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self._email = email
        self.__password = password
    
    def update_firstname(self, new_firstname):
         self.firstname = new_firstname
         return self.firstname

    def update_lastname(self, new_lastname):
        self.lastname = new_lastname
        return self.lastname

    def update_username(self):
        #self.firstname = new_firstname
        #self.lastname = new_lastname
        return f"{self.firstname} {self.lastname}"

    def update_email(self, new_email):
        self._email = new_email

    def update_password(self, new_password):
        self.__password = new_password
        
    def get_password(self):
        return self.__password
    
    def get_email(self):
        return self._email

user1 = user("Faith", "Adeosun", "Faith Adeosun", "adeosunfaith0101@gmail.com", "progress22#$")
print(user1)
print(user1.firstname)
print(user1.lastname)
print(user1.username)
print(user1._email)
#print(user1.__password)

print(user1.update_firstname("Esther"))
print(user1.update_lastname("Akande"))
print(user1.update_username())
print(user1.get_email())
(user1.update_email("funmito97@yahoo.com"))
print(user1.get_email())
print(user1.get_password())
(user1.update_password("success22#$"))
print(user1.get_password())

#print(user.othername)
#print(user1.othername)
#
#user.othername = "AFEX"
#print(user.othername)
#print(user1.othername)
#
#user1.othername = "AFTL"
#print(user.othername)
#print(user1.othername)