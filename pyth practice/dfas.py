
class Rectangle:
    #width = None
    #height = None
    
    def __init__(self, width, height = None):
        self.width = width
        self.height = height
        if height is None:
            self.height = self.width

    def perimeter(self):
        return self.height + self.width
    
    def area(self):
        return self.height * self.width
    
    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width, height)
    
    def __sub__(self, other):
        width = abs(self.width - other.width)
        height = abs(self.height - other.height)
        return Rectangle(width, height)
    
    def __lt__(self, other):
        first = self.width * self.height
        second = other.width * other.height
        return first < second
    
    def __eq__(self, other):
        first = self.width * self.height
        second = other.width * other.height
        return first == second

    def __le__(self, other):
        first = self.width * self.height
        second = other.width * other.height
        return first <= second
    
    def __repr__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")  
print(f"Площадь rect2: {rect2.area()}")    
print(f"rect1 < rect2: {rect1 < rect2}")        
print(f"rect1 == rect2: {rect1 == rect2}")   
print(f"rect1 <= rect2: {rect1 <= rect2}")     

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}") 
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")     