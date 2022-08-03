from math import sqrt, pi

class Shape:
    def __init__(self, name, no_of_sides, length):
        self.name = name
        self.no_of_sides = no_of_sides
        self.length = length

    def get_name(self):
        return self.name

    def get_no_of_sides(self):
        return self.get_no_of_sides

    def get_length(self):
        return self.length


class TwoDimensional(Shape):
    def __init__(self, name, no_of_sides, length):
        super().__init__(name, no_of_sides, length)

    def area(self):
        pass

    def perimeter(self):
        pass


class ThreeDimensional(Shape):
    def __init__(self, name, no_of_sides, length):
        super().__init__(name, no_of_sides, length)

    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass


class Square(TwoDimensional):
    def __init__(self, name, no_of_sides, length):
        super().__init__(name, no_of_sides, length)

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.no_of_sides * self.length


class Triangle(TwoDimensional):
    def __init__(self, name, no_of_sides, length, base, height):
        super().__init__(name, no_of_sides, length)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.length + self.base + self.height


class Rectangle(TwoDimensional):
    def __init__(self, name, no_of_sides, length, width):
        super().__init__(name, no_of_sides, length)
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Cube(ThreeDimensional):
    def __init__(self, name, no_of_sides, length):
        super().__init__(name, no_of_sides, length)

    def area(self):
        self.no_of_sides = 6
        return self.no_of_sides * (self.length ** 2)

    def perimeter(self):
        self.no_of_sides = 12
        return self.no_of_sides * self.length

    def volume(self):
        return self.length ** 3


class Sphere:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        
    def area(self):
       return 4 * pi * (self.radius**2)

    def perimeter(self):
        return 2*pi*self.radius

    def volume(self):
        return (4/3) * pi * (self.radius **3)


class Tetrahedral(ThreeDimensional):
    def __init__(self, name, no_of_sides, length):
        super().__init__(name, no_of_sides, length)

    def area(self):
        return round(sqrt(3 * self.length **2), 2) 

    def volume(self):
        return (round(sqrt(2 * self.length **3)/12, 2))

    def perimeter(self):
        return self.no_of_sides * self.length


shape1 = Square("square", 4, 3)
shape2 = Triangle("Triangle", 3, 5, 3, 4)
shape3 = Rectangle("Rectangle", 4, 5, 7)
shape4 = Circle("Circle", 6)
shape5 = Cube("Cube", 6, 1)
shape6 = Sphere("Sphere", 6)
shape7 = Tetrahedral("Tetrahedral", 6, 8)

print(shape1.perimeter())
print(shape5.area())
print(shape5.perimeter())
print(shape4.area())
print(shape4.perimeter())
print(shape7.area())
print(shape7.volume())
print(shape7.perimeter())