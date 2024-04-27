import numpy as np
# Different classes have same named mathod but different implementation

class Square:
    def __init__(self, l):
        self.l = l
    
    def getArea(self):
        return self.l * self.l
    
class Circle:
    def __init__(self, r):
        self.r = r
    
    def getArea(self):
        return self.r * np.pi

sq = Square(4)    
cir = Circle(5) 

print(f"{sq.getArea()}\n{cir.getArea()}")

# We can  define two function outside  the class with same name but with different numbers of parameter

def getMax(a, b):
    if a > b:
        return a
    return b

def getMax(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

print(f"Maximum of two numbers - from two argument function $=$ {getMax(5, 3, np.nan)}\nMaximum of two numbers - from two argument function $=$ {getMax(12, 23, 41)}")