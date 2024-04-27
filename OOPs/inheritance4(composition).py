# Composition

class Engine:
    def __init__(self, power):
        self.power = power

class Door:
    def __init__(self, material):
        self.material = material
    
class Car:
    def __init__(self, power, material, noOfDoors):
        self.engine = Engine(power)
        self.material = Door(material)
        self.noOfDoors = noOfDoors

x = Car(23, "Wood", 2342)

print(x.engine.power, x.noOfDoors)