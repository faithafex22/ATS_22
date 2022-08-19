

class Rectangle():
    def __init__(self, length=1.0, width=1.0):
        self._length = length
        self._width = width
        
    def perimeter(self):
        return  2 * (self._length  + self._width )
    
    def area(self):
        return self._length * self._width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        if length>0.0 and length<20.0:
            if isinstance(length, float) == True:
                self._length = length
            else:
                return "you have to input your length in float form e.g 2.0"
        else:
           return "your input is either too low or high, it shouldn't be < 0.0 and > 20.0"
    
    @property  
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width>0.0 and width<20.0:
            if isinstance(width, float) == True:
                self._width = width
            else:
                return "you have to input your width in float form"
        else:
            return "your input is either too low or high"
            
    
       
rectangle1 = Rectangle(2.0, 4.0)   

print(rectangle1.perimeter())
print(rectangle1.area())
print(rectangle1.length)
print (rectangle1.width)

rectangle1.length = 3.0
rectangle1.width = 5.0

print(rectangle1.perimeter())
print(rectangle1.area())
print(rectangle1.length)
print (rectangle1.width)

        