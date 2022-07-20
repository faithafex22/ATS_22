def change():
    num = input("Enter your credit card number here, it must be a 16 digits: ")
    newnum =  num[0:12]
    # for character in newnum:
    num = num.replace(newnum, "*"*(len(newnum)))
    print(num)
    # encode = newnum + othernums
    # print(encode)

change()