class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getLength(self):
        return self.__length
    
        # setter Method
    def setLength(self, length):
        self.__length = length

        # getter method
    def getwidth(self):
        return self.__width
    
        # setter Method
    def setwidth(self, width):
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)
dimesion = Rectangle(10, 3)

print(dimesion.area())
print(dimesion.perimeter())