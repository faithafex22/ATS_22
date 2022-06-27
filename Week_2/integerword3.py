def words(n): 
 units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"] 
 teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"] 
 tens = ["Twenty","Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
 if n <= 9: 
    return units[n] 
 elif n >= 10 and n <= 19: 
    return teens[n-10] 
 elif n >= 20 and n <= 99: 
    return tens[(n//10)-2] + " " + (units[n % 10] if n % 10 !=0 else "") 
 elif n >= 100 and n <= 999: 
    if n % 100 !=0:
        return words(n//100) + " Hundred And " + (words(n % 100))
    else:
        return words(n//100) + " Hundred"
 elif n >= 1000 and n <= 99999: 
    if n % 1000 !=0:
        return words(n//1000) + " Thousand " + (words(n % 1000))
    else:
        return words(n//1000) + " Thousand" 

print(words(980))

def cordinal(n):
   special = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th']
   if n== 1:
          
   if n >=4 and n <= 20:
      return str(n) + 'th'

   
   elif n[-1] == 1:
      return str(n) + "th"
   