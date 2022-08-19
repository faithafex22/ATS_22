import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
special = string.punctuation

def gen(name):
    password = " "
    a = random.choice(lower)
    b = random.choice(upper)
    c = random.choice(special)
    d = random.randrange(21, 99)
    e = str(d)
    f = random.choice(special)
    newname = list(name)
    password = password + f"{newname[0]}{a}{b}{c}{e}{f}{newname[-1]}"
    
    
    return password

print(gen("faith"))
    
