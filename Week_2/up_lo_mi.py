def determine(word):
   import string
   alpha_lower = string.ascii_lowercase
   alpha_upper = string.ascii_uppercase
 
   if word in alpha_lower:
      print("word is in lower case")
   elif word in alpha_upper:
     print("word is in upper case")
   elif word in alpha_lower and alpha_upper:
     print("word is a mixture of upper and lower case")

determine("Obey")