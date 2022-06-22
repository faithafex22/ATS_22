def up_low(s):
    a=list(s)       
    u=[]
    l=[]
    for x in a:
        if x.isupper():
            u.append(x)
        elif x.islower():
            l.append(x)
        else:
            pass  
    return u, l

u, l = up_low(s)        
print(f'No. of Upper case characters: {len(u)}')
print(f'No. of Lower case Characters: {len(l)}')

def count_upper_lower(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1

    print uppercase_letter_count, lowercase_letter_count
    

    def up_low(string):
      uppers = 0
      lowers = 0
    for char in string:
     if char.islower():
      lowers += 1
     elif char.isupper():
      uppers +=1
    else: #I added an extra case for the rest of the chars that aren't lower non upper
      pass
  return(uppers, lowers)

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))