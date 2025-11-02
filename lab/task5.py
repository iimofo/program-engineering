import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

rectangle = Rectangle(4, 5)
circle = Circle(3)

shapes = [rectangle, circle]

total_area = 0
print("\nCalculating areas:")
for shape in shapes:
    current_area = shape.area()
    print(f"Area: {current_area}")
    total_area += current_area
    
print(f"\nTotal Area: {total_area}")
