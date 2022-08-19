
from fractions import Fraction

class Rational():
    def __init__(self, num1=0, den1=0, num2=0, den2=0 ):
        self.num1 = num1
        self.num2 = num2
        self.den1 = den1
        self.den2 = den2
        
    def add(self):
        ans = Fraction(self.num1 ,self.den1 )+ Fraction(self.num2,self.den2)
        return ans
    
    def subtract(self):
        ans = Fraction(self.num1,self.den1) - Fraction(self.num2,self.den2)
        return ans
        
    def multiply(self):
        ans = Fraction(self.num1,self.den1) * Fraction(self.num2,self.den2 )
        return ans
        
    def divide(self ):
        ans = Fraction(self.num1,self.den1) / Fraction(self.num2,self.den2)
        return ans 
    def output(self):
        return Fraction(self.num1, self.den1)
    
    def offset(self):
        return  round(self.num1 /self.den1,  2)
    
    
rational1 = Rational(4, 6, 2, 4)  
print(rational1.add())  
print(rational1.subtract()) 
print(rational1.multiply()) 
print(rational1.divide()) 
print(rational1.offset()) 
print(rational1.output())