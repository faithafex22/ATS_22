#ussd or emulator
import random
import sys

balance = 50000

def set_pin():
    pin = (input("set your pin by entering a 4 digit number: "))
    if len(pin) != 4:
        print("Error the number of digits must be 4")
        return set_pin()
    print(f"you have successfully set your pin -> {pin}")
    return pin 
PIN = set_pin() 


def get_balance():
    
    input_pin = (input("Enter your ussd pin here to check your balance: "))
    if input_pin == PIN:
        print(f"your balance is  #{balance}")
        return balance
    return("The pin entered is incorrect, ypu can reset your pin")
acct_balance = get_balance()

def transfer():
    global balance, PIN
    amount = int(input("Enter the amount you want to transfer: "))
    for x in range (3, 0, -1):
        if amount <= balance:
            for y in range (3, 0, -1):
                recipient = input("Enter the recipient account no: ")
                if len(recipient) == 10:
                    input_pin = input("please enter your ussd pin here: ")
                    if input_pin == PIN:
                        print(f"transfer is successful, your remaining balance is {balance - amount}")
                        balance = balance - amount
                        return balance
                    return("incorrect pin, you can reset your pin")
                else:
                    return(f"invalid account number, kindly recheck, you have {y-1} tries left")
        else:
            return (f"insufficient balance, amount is greater than balance, you have {x-1} tries left")
transfer_cash = transfer()

def buy_airtime():
    global balance, PIN
    input_pin = (input("Enter your ussd pin to load airtime: "))
    if input_pin == PIN:
        owner =  input("Type \"1\" to purchase airtime for Self or \"2\" to load for 3rd party: ") 
    else:
        print("invalid ussd pin, you can reset your pin")
    if owner == "1" or "2":
        amount = int(input("Enter the amount of recharge card you want to purchase: "))
    if owner == "1" and balance > amount:
        print(f"you have successfully recharge your line with #{amount} credit card, your available balance is {balance-amount}")
        balance = balance - amount
        return balance
    elif owner == "2" and balance > amount:
        recipient = input("Enter the recipient phone number: ")
    else: 
        print("avaialble balance is insufficient for amount of airtime purchase")
    if recipient != None:
        print(f"you have successfully recharge {recipient} with #{amount} credit card, your available balance is {balance-amount}")
        balance = balance - amount
        return balance
    else:
        print("invalid phone_no, please check your entry")
airtime_purchase = buy_airtime()

def buy_data():
    global balance, PIN
    input_pin = (input("Enter your ussd pin to load data: "))
    if input_pin == PIN:
        owner =  input("Type \"1\" to purchase data for Self or \"2\" to load for 3rd party: ") 
    else:
        print("invalid ussd pin, you can reset your pin")
    if owner == "1" or "2":  
        datadict = {"1":[100,100],"2":[300, 350], "3":[750, 500], "4":[1000, 300], "5":[1500, 1000]}
        print("Select a data bundle")
        print("1) 100MB 1day N100")
        print("2) 350MB 7days N300")
        print("3) 750MB 14days N500")
        print("4) 1GB 1day N300")
        print("5) 1.5GB 30days N1000")
        selected = input("Enter number here: ")
        datacost = datadict[selected][1]
        datamb = datadict[selected][0]
    if owner == "1" and datacost < balance:
        print(f"you have succesfully purchase a data of #{datacost}, your new data balance is {datamb}mb and your new account balance is #{balance-datacost}")
        balance = balance - datacost
        return balance
    elif owner == "2" and datacost < balance:
        recipient = ("Enter recipient phone no: ")
    else: 
        print("avaialble balance is insufficient for amount of data purchase")
    if recipient != None:
            print(f"you have successfully recharge {recipient} with #{datamb}mb data, your available balance is {balance-datacost}")
            balance = balance - datacost
            return balance
    else:
        print("invalid phone_no, please check your entry")
purchase_data = buy_data()
    
def generate_otp():
    otp = ""
    for i in range(0, 4):
        otp = otp + str(random.randint(0, 9))
    print(f"your otp pin generated is {otp}")
otp_generation = generate_otp()
            
def user():
    global balance, PIN
    name = input("Welcome user, what is your name?: ")
    ussd_dict = {
    "*901#" : "Acess Bank",
    "*326#" : "Ecobank",
    "*770#" : "Fidelity Bank",
    "*894#" : "First Bank",
    "*389*214#": "FCM Bank",
    "*737#": "GT Bank",
    "*322*00#": "Heritage Bank",
    "*7111#": "Keystone Bank",
    "*833#": "Polaris Bank",
    "*909#": "IBTC Bank",
    "*822#": "Sterling Bank",
    "*919#": "UBA",
    "*826#": "Union Bank",
    "*7799#": "Unity Bank",
    "*945#": "Wema Bank",
    "*966#": "Zenith Bank"
    }
    ussd_code = input(f" welcome {name.title()}, enter your bank ussd code: ")
    if ussd_code in ussd_dict:
        print(f"""
            Welcome to {ussd_dict[ussd_code]}, {name.title()}.... 
            before you proceed, you will be charged #6.80 for any transaction you make
                  """)
        option = input("if you agree to our term type \"1\", if not, type \"2\": ") 
        if option == "1":
            while True:
                input_pin = input("Enter your ussd pin to carry out an operation: ")
                if input_pin == PIN:
                    print("which of these operations will you like to carry out?")
                    print("1) Check Balance")
                    print("2) Transfer Cash")
                    print("3) Load Airtime")
                    print("4) Load Data")
                    print("5) Generate Otp")
                    print("6)  Exit\n")
    
                    operation = int(input("Enter number for the operation to perform: "))
                    ussd_dict = {1: get_balance, 2: transfer , 3: buy_airtime, 4: buy_data, 5: generate_otp, 6: sys.exit}
                    print(ussd_dict[operation]()) 
                else:
                    print("incorrect ussd pin, check your entry and enter once again")
        elif option == 2:
            print("thank you for banking with us")
    else:    
        print("invalid bank code, try again later")

user1 = user()