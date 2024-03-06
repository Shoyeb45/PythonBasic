class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # defining behaviour - method
    def dance(self):
        print(f"{self.name} can dance")
    

per1 = Person("Aditya", 18)

per1.dance()