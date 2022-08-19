
class Recordinate():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.set_function()
        
    def set_function(self):
        self.A = self.x1 , self.y1
        self.B = self.x2 , self.y2
        if self.x1<20 and self.x2<20:
            if self.y2<20 and self.y2<20:
                return self.A , self.B
            return "each of your parameter should not be more than 20"
                
    def get_dimensions(self):
        self.dim1 = self.x2 - self.x1
        self.dim2 = self.y2 - self.y1
        return self.dim1 , self.dim2
    
    def get_length(self):
        self.length = max(self.dim1, self.dim2)
        return self.length
    
    def get_width(self):
        self.width = min(self.dim1, self.dim2)
        return self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def ifsquare(self):
        if self.length == self.width:
            return "this is a square"
        else:
            return "this is a rectangle"
            
            
record1 = Recordinate(2, 3, 4, 6)
print(record1.set_function())
print(record1.get_dimensions())
print(record1.get_length())
print(record1.get_width())
print(record1.perimeter())
print(record1.area())
print(record1.ifsquare())