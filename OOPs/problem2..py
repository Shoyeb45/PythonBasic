import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sqNum(self):
        return self.x * self.x + self.y * self.y + self.z * self.z
    

vector = Point(2, 4, math.sqrt(5))

modulus = math.sqrt(vector.sqNum())

print(f"({vector.x}, {vector.y}, {vector.z}) has magnitude of {modulus}")