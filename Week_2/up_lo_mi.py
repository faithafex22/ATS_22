import string

alpha_lower = string.ascii_lowercase
alpha_upper = string.ascii_uppercase

al = set(string.ascii_lowercase)
ph = set(string.ascii_uppercase)
def determine(word):
  s = set(word)
  if s <=  al:
    print("word is in lower case")
  elif s <= ph:
    print("word is in upper case")
  else:
    print("word is a mixture of upper and lower case")

determine("Obey")