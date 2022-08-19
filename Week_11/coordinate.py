from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x =  self.x + x
        self.y = self.y + y
        return (self.x, self.y)
    
    def dis(self, point) :
        return sqrt((point.x-self.x)**2 + (point.y-self.y)**2)
        
p1 = Point (2,3)
print(p1.show())
p2 = Point(4,5)
print (p2.show())
p1.move(5, 5)
print(p1.show())
p2.move(6,6)
print(p2.show())
print(p1.dis(p2))

