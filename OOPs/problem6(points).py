import  math
import numpy as np

# class with points

class Point:
    # Initializer
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # distance
    def EuclideanDistance(self):
        return round(math.sqrt(self.x**2 + self.y**2 + self.z**2), 4)
    
    # distance for two poitns
    def distance(self, p):
        return round(math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2), 4)
    
    # Points are equal or not
    def isEqual(self, p):
        if self.x == p.x and self.y == p.y and self.z == p.z:
            return True
        
        return False
    
    # Cross product
    def cross(self, p):
        X = self.y * p.z - self.z * p.y
        Y = -(self.x * p.z - p.x * self.z)
        Z = self.x * p.y - p.x * self.y

        return Point(round(X, 3), round(Y, 3), round(Z, 3))
    
    # dot Product
    def dot(self, p):
        return round(self.x * p.x + self.y * p.y + self.y * p.y, 4)
    
    # Unit Vector
    def unit(self):
        mod = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

        return Point(round(self.x/mod, 3), round(self.y/mod, 3), round(self.z/mod, 3))
    
    # Rotate about point, angle in degree
    def rotate(self, ang, axis):
        ang = round((ang * np.pi)/180, 3)
        
        if axis == 'X':
            rotationMatrixX = np.array([[[np.cos(ang), -np.sin(ang), 0], 
                                   [np.sin(ang), np.cos(ang), 0], 
                                   [0, 0, 1]]])
            p = np.array([self.x, self.y, self.z])

            resultant = rotationMatrixX @ p
        elif axis == "Y":
            rotationMatrixY = np.array([[[np.cos(ang), 0, np.sin(ang)], 
                                   [0, 1, 0], 
                                   [-np.sin(ang), 0, np.cos(ang)]]])
            resultant = rotationMatrixY @ p
        else:
            rotationMatrixZ = np.array([[[1, 0, 0], 
                                   [0, np.cos(ang), -np.sin(ang)], 
                                   [0, np.sin(ang), np.cos(ang)]]])
            resultant = rotationMatrixZ @ p

        
        X = resultant[0][0]
        Y = resultant[0][1]
        Z = resultant[0][2]
        return Point(round(X, 3), round(Y, 3), round(Z, 3))




p1 = Point(1, 2, 0)
p2 = Point(1, 2, 1)
p3 = p1.cross(p2)
p4 = p2.unit()

print(p3.x, p3.y, p3.z)
print(p4.x, p4.y, p4.z)
print(p1.distance(p2))
print(p1.isEqual(p2))

p5 = p1.rotate(60, "X")
print(p5.x, p5.y, p5.z)