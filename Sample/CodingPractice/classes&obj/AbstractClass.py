from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b
    
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5*self.b*self.h

r = Rectangle(2, 4)
print(r.area())
t = Triangle(3, 2)
print(t.area())