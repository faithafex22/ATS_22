

from datetime import date
class User:
    othername = "ATS" #class variable or attribute
    noofuser = 0
    #def__init__ is a constructor
    def __init__(self, firstname, lastname, username, email, password):
    #instance variables or attribute
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self._email = email
        self.__password = password
        User.noofuser += 1
       
    def update_firstname(self, new_firstname):
         self.firstname = new_firstname
         return self.firstname
    
    def update_lastname(self, new_lastname):
        self.lastname = new_lastname
        return self.lastname
   
    #def update_username(self, firstname, lastname):
        #return f"{self.firstname} {self.lastname}"
    #@update_username.setter
    def update_username(self, new_firstname, new_lastname):
        self.firstname = new_firstname
        self.lastname = new_lastname
        return f"{self.firstname} {self.lastname}"

    def add_thirdname(self):
        addthirdname = self.username + " " + self.othername #this should be used when othername is different for each instances, i.e object
        return addthirdname                                 #but when it is thesame use class variable

    def update_email(self, new_email):
        self._email = new_email

    def update_password(self, new_password):
        self.__password = new_password
        
    def get_password(self):
        return self.__password
    
    def get_email(self):
        return self._email

    @classmethod #-> this is called decorators
    def set_othername(cls, othername):
        cls.othername = othername
    #notice classmethod can be used to call static method e.g cls.birth_day(age)

    @classmethod
    def from_string(cls, user_str):
        firstname, lastname, username, email, password = user_str.split("-")
        return cls(firstname, lastname, username, email, password)

    @staticmethod #decorators
    def birth_day(age):
        dateofbirth = date.today().year - age
        return dateofbirth

    #def __repr__(self):
       # return f"{self.firstname}, {self.lastname}, {self.username}, {self._email}, {self.__password}"

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.username}, {self._email}, {self.__password}"
    def __add__(self, other):
        return self.username +" " + other.othername   

    def __len__(self):
        return len(self.add_thirdname())   

class Developer(User):
    othername = "software engineer"
#what do you do when you have an attribute for the new class that can't be inherited from the former class because it does not have it?
#let us go
    def __init__(self, firstname, lastname, username, email, password, prog_language):#the last attribute here was just created pertaining to class Developer
        super().__init__(firstname, lastname, username, email, password)
        self.prog_language = prog_language

class Manager(User):
    def __init__(self, firstname, lastname, username, email, password, employees=None):#the last attribute here was just created pertaining to class Developer
        super().__init__(firstname, lastname, username, email, password)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    def print_employee(self):
        for employee in self.employees:
            print(employee.username)

    


#print(User.noofuser)
dev1 = Developer("Faith", "Adeosun", "Faith Adeosun", "adeosunfaith0101@gmail.com", "progress22#$", "python")
#user_str1 = "Oluwatoyin-Bankole-Oluwatoyin Bankole-olueunice27@gmail.com-provision22#$"
#user_str2 = "Mercy-Ajiboso-titiaji25@yahoo.com-soaring22@%"

#new_user1 = User.from_string(user_str1)
dev2 = Developer("Oluwatoyin", "Bankole", "Oluwatoyin Bankole", "olueunice27@gmail.com", "provision22#$", "java")

mang1 = Manager("Mercy", "Ajiboso", "Mercy Ajiboso", "titiaji@yahoo.com", "soaring22@$", [dev1])

#mang1.print_employee()
mang1.add_employee(dev2)
mang1.remove_employee(dev1)
mang1.print_employee()
print(isinstance(mang1, Manager))
print(issubclass(Developer, User))
print(dev1.__len__())

dev1.username = "Esther Akande"
print(dev1.username)
#print(dev1 + dev2)
#print (new_user1._email)
#print(dev1.prog_language)
#print(dev1.birth_day(25))
#print(dev1.username)
#print(dev1.add_thirdname()) 
#print#(user1.lastname)
#print#(user1.username)
#print#(user1._email)
##prit#t(user1.__password)t#print(user1.update_firstname("Esther"))
#print#(user1.update_lastname("Akande"))
#print#(user1.update_username("Esther", "Akande"))
#print#(user1.get_email())
#(uset#1.update_email("funmito97@yahoo.com"))
#print#(user1.get_email())
#print#(user1.get_password())
#(uset#1.update_password("success22#$"))
#print#(user1.get_password())
#print#(user1.__dict__)
#print#(user1.add_thirdname())
#print#(User.noofuser)t#User.set_othername("AFITL")
#print#(User.othername)
#print#(user1.othername)
#t#
#t#User.othername = "AFEX"
##prit#t(User.othername)
##prit#t(user1.othername)
#t#
#t#user1.othername = "AFTL"
##prit#t(User.othername)
##prit#t(user1.othernamet#