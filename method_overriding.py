class shape:
    def area(self):
        return 0
    
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
class Square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    
s1=Square(4)
c1=Circle(3)

print(s1.area())
print(c1.area())
