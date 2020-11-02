from math import pi
class Circle():
    def __init__(self,radius):
        self.radius=radius

    def calculatePerimeter(self, radius):
        perimeter = 2*pi*radius
        return perimeter

