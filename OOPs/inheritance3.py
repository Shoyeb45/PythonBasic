# has a relation - can be implemented as Aggregation and composition


# Aggregation
class Engine:
    def __init__(self, power):
        self.power = power

class Door:
    def __init(self, material):
        self.material = material

class Car:
    def __init__(self, engine ,door, numberOfDoors):
        self.engine = engine
        self.door = door
        self.numberOfDoors = numberOfDoors


e = Engine(134)
d = Door("Titanium")
c = Car(e, d, 5)
# The existence of object of Engine and Door are independent of class Car, if we delete 