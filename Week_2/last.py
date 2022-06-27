import string

alphabets = string.ascii_lowercase
alphabets_list = list(alphabets)
del alphabets_list [0:16]

print(alphabets_list)