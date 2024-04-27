# Private attribute will only be accessible for parent class
# Protacted and public attributes can be accessed for both the classes

class Vehicle:
    def __init__(self, name):
        self.__name = name

    def display(self):
        print(f"I am a {self.__name} vehicle.")

    def getName(self):
        return self.__name
    

class Car(Vehicle):
    pass
    def type(self):
        print(f"Car name is {self.getName()}")

x = Car("Jaguar")

x.display()
x.type()

# Shape class

class Shape:
    def __init__(self, sides):
        self.sides = sides

    def getNumberOfSides(self):
        return self.sides
    
class Sqaure(Shape):
    def __init__(self, length):
        self.length = length
        super().__init__(4)

sq = Sqaure(5)
print("Number of sides",sq.sides)
sq.sides = 9
print("Number of sides",sq.sides)
print("Side length",sq.length)