
class Complexnum():
    def __init__(self, real1 =0, imag1=0j, real2=0, imag2=0j):
        self.real1 = real1
        self.imag1 = imag1
        self.real2 = real2
        self.imag2 = imag2
        
    def add(self):
     ans = complex(self.real1, self.imag1) + complex(self.real2, self.imag2)
     return ans
    
    def subtract(self):
        ans = complex(self.real1, self.imag1) - complex(self.real2, self.imag2)
        return ans
    def output(self):
        ans = complex(self.real1, self.imag1)
        return ans
        
        
        
        
        
compnum1 = Complexnum(2, 3, 4, 5)
print(compnum1.add())
print(compnum1.subtract())
print(compnum1.output())