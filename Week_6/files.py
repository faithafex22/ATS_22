# with open("STAR.txt", mode="a") as file:
#     print(file.write("look"))



#with open("STAR.txt", mode="a") as file:
    #print(file.writelines("\nthe day is bright," "is bright and fair," "noh happy day," "the day of joy"))

#with open("new.txt", mode="r") as file:
    #print(file.read().split())

with open("new.txt", "r") as fi , open("formatted_new.txt", "w") as fo:
    lines = (fi.readlines())
    for line in lines:
        if line != " ":
            line.strip()
            fo.write(line.strip())
            fo.write('\n')


#firstname = input('Enter your firstname: ')
#lastname = input('Enter your lastname: ')
#username = firstname + " " + lastname
#password = input('Enter your password: ')
#confirm_password = input('confirm your password: ')
#if password != confirm_password:
#    print("incorrect password")
#filename = username + ".txt"
#with open(filename, "w") as data:
#print(data.writelines(f'Firstname: {firstname}\nLastname: {lastname}\nUsernmae: {username}\nPassword: {password}\nConfirm_password: {confirm_password}'))
