
def operations():
    name = "Faith Adeosun"
    phoneno = +2348104431262
    otppin = 1997
    confirm = 1997
    person = [name, phoneno, otppin, confirm]
    balance = 10000
    bankcode = 737
    majorop  = {"1.": "Check Balance", "2.": "Buy Airtime", "3.": "Buy Data", "4.": "Transfer Cash" }
    dataplans = {"daily": "1gb for #300", "weekly": "6gb for #1500", "monthly": "20gb for #5000"}
    print(person)
    
    bankcode == input("enter your bankcode: ")
    if bankcode == 737:
        print("proceed")
    else:
        print("you entered an invalid pin")
    if input == "proceed":  
        print(majorop)
    else:
        print("operation cancelled")
    if input == majorop["1."]:
        print("enter your otppin to check balance")
        for i in person:
            if otppin == otppin and phoneno == phoneno:
                print(balance)
            else:
                print("invalid pin or no not yet registered")
    else:
        for i in majorop:
            continue;
    
    if input == majorop["2."]:
        print("enter your otppin to buy airtime")
        for i in person:
            if otppin == otppin and phoneno == phoneno:
                input("enter the amount of airtime you want to buy: ")
                if input < balance: 
                    print("airtime successfully purchased")
                elif input >= balance:
                    print("limit exceeded") 
            else:
                print("invalid pin or invalid phoneno")
    else:
        for i in majorop:
            continue;
            
     
    if input == majorop["3."]:
        print("enter your otppin to buy data")
        for i in person:
            if otppin == otppin and phoneno == phoneno:
                print(dataplans)
                input("select a data plan: ")
            else:
                print("incorect pin")
            if input in dataplans and input < balance:
                print("data purchase successful")
            else:
                print("input not in dataplans or limit exceeded")
    else:
        for i in majorop:
            continue;
    
    if input == majorop["4."]:
       input("enter your otppin to make transfer")
       for i in person:
            if otppin == otppin and phoneno == phoneno:
               input("enter the amount you want to transfer: ")
            else:
                print("otppin is incorrect")
            if input < balance:
                input("enter the beneficiary account no or name: ")
                input("enter the bank you are transferring to: ")
                print("transfer successful")
            else:
                print("limit exceeded or some entries are incorrect")
    else:
        print("what transaction do you want to carry out?, go back to the main menu")

    if input != majorop["1."] or input != majorop["2."] or input != majorop["3."] or input != majorop["4."]:
        print("transaction does not exist")


print(operations())
