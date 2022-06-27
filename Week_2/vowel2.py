
import string

alpha_lower = string.ascii_lowercase

alphabet = list(alpha_lower)

vowels= ['a','e','i','o','u']
a = []
b = []
for char in alphabet:
  if char in vowels:
                a.append(char)

for char in alphabet:
    if char not in vowels:
        b.append(char)      

print(a)
print(b)
