# Super usecases:
# 1. Initializer :

class Parent:
    country = "India"
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Parent is eating")
    
class Child(Parent):
    country = "USA"
    def __init__(self, name, age):
        super().__init__(name)

    def whereDoILive(self):
        print(f"My parents live in {super().country}")
        print(f"I live in {self.country}")

    def eat(self):
        print("Child is eating")

    def eatingPattern(self):
        super().eat()
        self.eat()

stud1 = Child("Shoyeb", 19)
stud1.eatingPattern()
stud1.whereDoILive()