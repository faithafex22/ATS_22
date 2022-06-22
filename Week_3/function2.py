#Write a function that takes a two strings as an argument and prints if the first string is a substring of the second.
#Write a function that converts a string to uppercase and returns the result.
#Write a function that converts a string to lowercase and returns the result.
#Write a function that converts a string to titlecase and returns the result.
#Write a function that converts the first letter of each word in a sentence to uppercas
#Write a function that checks if a string contains both alphabets and numbers.

def two(x:str,y:str):
    if x in y:
        return True;
    else:
        return False;

print(two('formation', 'information'))

def convert1(b:str):
    y = b.upper()
    return y;

print(convert1('fellow'))

def convert2(c:str):
    a = c.lower()
    return a;

print(convert2('PEOPLE'))

def convert3(d:str):
    e = d.title()
    return e;

print(convert3('father'))

def convert3(i:str):
    j = i.title()
    return j;

print(convert3('i love playing around with python data types'))

def checking(g):
    if g.isalnum():
        return True;
    else:
        return False;

print(checking('*^abc12'))
