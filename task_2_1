import math

class Dot:
    def __init__(self,x,y,color = None):
        self.x= x
        self.y= y
        self.color= color
    
    def __str__(self):
        return f"{self.x},{self.y},{self.color}"
    
    def set_color(self,color):
        self.color = color
        
class Circle(Dot):
    def __init__(self,x,y,color,radius = 1):
        super().__init__(x,y,color)
        self.radius = radius
    
    def __str__(self):
        return f"{self.x},{self.y},{self.color},{self.radius}"
    
    def area(self):
        return math.pi * (self.radius**2)

    def set_radius(self,radius):
        self.radius = radius

class Sphere(Circle):

    def volume(self):
        return (4 / 3) * math.pi * self.radius**3

    def area(self):
        return 4*math.pi*self.radius**2
    


dot = Dot(10,10)
dot.set_color('Blue')
print(dot)
print('***')

circle = Circle(30,30,None, 30)
circle.set_color('Blue')
print(circle)
print(circle.area())
circle.set_radius(10)
print(circle)
print('***')
         
sphere = Sphere(30,30,10)
print(sphere)
print(sphere.volume())
print(sphere.area())
print('***') 
