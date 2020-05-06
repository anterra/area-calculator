import math


class Rectangle:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def area(self):
        area = self.length1 * self.length2
        return area


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area


while True:
    shape = input("Area Calculator. Is your shape a rectangle or a circle? ")
    if shape == "rectangle":
        length1 = int(input("What is the width? "))
        length2 = int(input("What is the second height? "))
        my_shape = Rectangle(length1, length2)
        print(my_shape.area())
        break
    elif shape == "circle":
        radius = int(input("What is the radius? "))
        my_shape = Circle(radius)
        print(my_shape.area())
        break
    else:
        break
