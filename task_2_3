#     Написать класс точка.
#         __init__, внутри которого будут определены координаты точки по осе абсцисс и ординат.
#         Начальные значения свойств берутся из входных параметров метода.
#         __str__ и/или __repr__ – x,y, цвет точки
#         методset_color, который задает цвет точки
#
#     Написать класс круг.
#         класс является потомком класса точка
#         __init__, внутри которого будут определены: координаты центра окружности и радиус
#         __str__ и/или __repr__ – x,y, радиус, цвет круга
#         метод area – возвращает площадь круга
#         метод set_radius -- позволяет изменить радиуса окружности
#
#     Написать класс сфера.
#         класс является потомком класса окружность
#         __init__, внутри которого будут определены: координаты центра, радиус.
#         метод volume – возвращает площадь круга
#         подумайте о том, как быть с методом area

from abc import ABC, abstractmethod
from enum import Enum, unique
import math

@unique
class Color(Enum):
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    PURPLE = 5

class Figure(ABC):

    classname = None

    @abstractmethod
    def __init__(self,x: int,y: int, color: Color):
        self._x = x
        self._y = y
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color = value
        
    def __str__(self):
        return f'{self._x},{self._y}' 

class Circle(Figure):
    def __init__(self,x,y,r,color):
        super().__init__(x,y,color)
        self._r = r
    
    def __str__(self):
        return f'{self._x},{self._y},{self._r},{self._color}' 
    
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        if value < 0:
            self._r = 0
        else:
            self._r = value
    
    def area(self):
        return math.pi * (self._r**2)
    
class Sphere(Circle):
    def __init__(self,x,y,r):
        super().__init__(x,y,r)

    def volume(self):
        return 4 / 3 * math.pi * self._r**3

    def area(self):
        return 4*math.pi*self._r**2
    
    def __str__(self):
        return f'{self._x},{self._y},{self._r},{self._color}' 
    
