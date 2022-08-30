import string
def encode (data:str):
    digits = string.digits 
    scharr = string.punctuation
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    rev_alpha_lower = alpha_lower[::-1]
    vowels = ["a", "e", "i", "o", "u"]
    vowels_map = ["@", "#", "$", "%", "&"] 
    enc = list()
    for s in data:
        if s.lower() in vowels:
            enc.append(vowels_map[vowels.index(s)])
        elif s in scharr:
            enc.append("|" + s)
        elif s in alpha_lower or s in alpha_upper:
            enc.append(s.swapcase())
        elif s in digits:
            enc.append("^" + rev_alpha_lower[digits.index(s)])
    print("".join(enc))
encode(input("Enter a word: "))
