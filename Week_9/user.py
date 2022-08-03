#Create a user class, wallet, transaction class
#Each of the other classes should inherit from the User class
#Update your code such that some operations can be perform on the user class such as
#Creating a user
#Deleting
#Funding the wallet
#Logging transaction
import random 
from datetime import datetime
from decimal import Decimal
import sys


class Wallet():
    logs = []
    def __init__(self, username, bank_account, init_bal = 0):
        self.__username = username
        self.bank_account = bank_account
        self.__account_bal = init_bal
        self.date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    @property
    def account_bal(self):
        return self.__account_bal

    @account_bal.setter
    def account_bal(self, acc_bal):
        if acc_bal < 0:
            raise ValueError('Balance must be >= 0')
    
    def fund_wallet(self):
        amount = int(input("Enter the amount you want to fund: "))
        if amount < 0.0:
            raise ValueError("Amount must be a positive integer")
        print(self.__account_bal, amount)
        self.__account_bal = self.__account_bal + amount
        Wallet.logs.append (f"Name:{self.__username} \nDate:{self.date} \nDeposited:{amount}, \nAvailable_Balance:{self.__account_bal}")
        return f"Transaction successful, you just fund your account with #{amount}"

    def get_balance(self):
        return f"{self.__username}, you have #{self.__account_bal} in your wallet"

    def withdraw_to_bank(self):
        amount = int(input("Enter the amount you want to withdraw"))
        if self.__account_bal < amount:
            print("you have insufficient balance")
        else:
            self.__account_bal = self.__account_bal - amount
            Wallet.logs.append(f"Name:{self.__username}\n Date:{self.date}\n Withdrawn:{amount}to {self.bank_account}\n Available_Balance:{self.__account_bal}")
            return(f"transaction successful, you have #{self.__account_bal} left in your wallet")


class User:
    def __init__(self, username, email, bank_account, init_bal):
        self.__username = username
        self.__email = email
        self.bank_account = bank_account
        self.init_bal = init_bal
        self.wallet = Wallet(username, bank_account, init_bal=self.init_bal)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if username.isalpha() == False:
            raise ValueError("input is incorrect")
        self.__username = username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if "@.com" not in email:
            raise ValueError(f"{email} format is not correct")
        self.__email = email

    @staticmethod
    def generate_userid():
        id =""
        for _ in range(4):
            id =  id + str(random.randint(0, 9))
        return id

    @classmethod
    def create_user(cls, username, email, bank_account, init_bal):
        return cls(username, email, bank_account, init_bal)

    def del_user(self):
        pass

    def __repr__(self):
           return f" {self.__username}, {self.__email}, {self.bank_account}, {self.__init_bal}"



print('Welcome!, \nRegister your details first')
username = input('Username: ')
email = input('Email: ')
bank_account = input('Account Number: ')
init_bal = Decimal(input('Amount to open account with: '))

user2 = User.create_user(username=username, email=email, bank_account=bank_account, init_bal=init_bal)
print("Just something")

while True:
    option = input("""
        Select an action to perform:
        1. Fund Wallet
        2. Get Balance
        3. Withdraw to Bank
        4. Get all transaction logs
        5. Exit
    """)
    if option == '1':
        print(user2.wallet.fund_wallet())
        pass
    elif option == '2':
        print(user2.wallet.get_balance())
    elif option == '3':
        print(user2.wallet.withdraw_to_bank())
    elif option == '4':
        [print(x) for x in user2.wallet.logs]
    elif option == '5':
        sys.exit()
