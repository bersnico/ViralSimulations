import math
import random
import pgzrun
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other_point):
        return math.sqrt(((self.x-other_point.x)**2)+((self.y-other_point.y)**2))
    def move(self, vector):
        self.x += vector.h
        self.y += vector.v
    def makeVectorTo(self, other_point):
        return Vector((other_point.x-self.x), (other_point.y-self.y))
class Vector:
    def __init__(self, h, v):
        self.h = h
        self.v = v
    def add(self, other_vector):
        self.h += other_vector.h
        self.v += other_vector.v
    def subtract(self, other_vector):
        self.h -= other_vector.h
        self.v -= other_vector.v
    def multiply(self, multiple):
        self.h *= multiple
        self.v *= multiple
    def divide(self, divisor):
        if divisor != 0:
            self.h /= divisor
            self.v /= divisor
        else:
            print("***DID NOT DIVIDE BY ZERO***")
    def length(self):
        return math.sqrt((self.h**2) + (self.v**2))
    def normalize(self):
        length = self.length()
        if length != 0:
            self.h /= length
            self.v /= length
        else:
            print("***DID NOT DIVIDE BY ZERO***")

GREEN = "#42f45f"
RED = "#f44141"
WIDTH = 800
HEIGHT = 600

# ###Testing Point Class###
# point1 = Point(1,2)
# point2 = Point(1,5)
# print(point1.distance(point2), "should be 3")
# vec1 = point1.makeVectorTo(point2)
# print(vec1.h, vec1.v, "should be 0,3")
# vec2 = Vector(4,5)
# point2.move(vec2)
# print(point2.x, point2.y, "should be 5,10")

# ###Testing Vector Class###
# vec3 = Vector(5,0)
# vec3.normalize()
# print(vec3.h, vec3.v, "should be 1,0")
# vec4 = Vector(3,4)
# vec5 = Vector(1,2)

# print(vec4.length(), "should be 5")
# vec4.subtract(vec5)
# print(vec4.h, vec4.v, "should be 2, 2")
# vec4.add(vec5)
# print(vec4.h,vec4.v, "should be 3,4")

# ###Testing Movement###
# class Circle:
#     def __init__(self,x,y):
#         self.position = Point(x,y)
#         self.vel = Vector(random.uniform(-2,2),random.uniform(-2,2))
#     def moving(self):
#         self.position.move(self.vel)

#         if self.vel.length() >= 2:
#             self.vel.normalize()
#             self.vel.multiply(2)
#     def shape(self):
#         screen.draw.filled_circle((self.position.x,self.position.y),7,"white")
# c1 = Circle(300,300)
