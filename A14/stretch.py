class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"Circle Area:{3.14*self.radius**2}")

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f"Square Area:{self.side**2}")

class Rectangle(Shape):
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def area(self):
        print(f"Rectangle Area:{self.len*self.bre}")

c=Circle(5)
s=Square(6)
r=Rectangle(10,12)

c.area()
s.area()
r.area()
