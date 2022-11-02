from abc import ABC, abstractmethod
import math
class Figure(ABC):
    def __init__(self, nameFigure, colorFigure):
        self.nameFigure = nameFigure
        self.color = colorFigure

    @abstractmethod
    def findSquare(self):
        pass

class Circle(Figure):
    def __init__(self,nameFigure, colorFigure, radius):
        super().__init__(nameFigure, colorFigure)
        self.radius = radius

    def findSquare(self):
        print(f'Площадь {self.nameFigure}: {math.pi * math.pow(self.radius, 2)}')

class Triangle(Figure):
    def __init__(self,nameFigure, colorFigure, a, h):
        self.a = a
        self.h = h
        super().__init__(nameFigure, colorFigure)

    def findSquare(self):
        sq = 0.5 *(self.a * self.h)
        print(f'Площадь {self.nameFigure}: {sq}')


class Predator(ABC):
    @abstractmethod
    def hunting(self):
        pass

class Tiger(Predator):
    def hunting(self):
        print('Охотиться один')

    def climbtoTree(self):
        pass

class Lion(Predator):
    def hunting(self):
        print('Охоиться со стаей')

    def speedLimithigh(self):
        pass

# class Ligr(Tiger, Lion):
#     pass

c1 = Circle('Большой круг', 'красный', 4)
c1.findSquare()

t1 = Triangle('Треугольник в Египте', 'Желтый', 4, 6)
t1.findSquare()

"""
Создать классы Square, Romb, Rectangle
#Найти площать квадрата
#Найти площадь ромба
#Найти площадь прямоугольника 
"""






