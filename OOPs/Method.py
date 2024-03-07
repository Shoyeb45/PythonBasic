# Methods are of three types : 1) Instance methd, 2) Class Method, 3) Static Method

# class method - features:
# 1. We don't need instance (or object)
# 2. cls is paramter which can access class property
# 3. All object will have access to class method

# Static method - features:
# 1. It does not have acces to the class property and instance
# 2. We can call this method also like class methiod without need of creating new object

# Static method - features:
# 1. It does not have acces to the class property and instance
# 2. We can call this method also like class methiod without need of creating new object

class Person:
    country = "India"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
# 1. class method 
    @classmethod   # decorators
    def gaming(cls):
        print("We love to play games")
    # we can access the class property
        print(f"I love {cls.country}")


# 2. Static Method
    @staticmethod
    def massBunking():
        print("Bunking is good")


per1 = Person("Shoyeb", 19)
# class method
print("Class Method")
Person.gaming()  # calling without object
per1.gaming()

# static method
print("\nStatic Method:")
Person.massBunking()


# 3. Instance method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # defining behaviour - method
    def dance(self):
        print(f"{self.name} can dance")
    

per1 = Person("Aditya", 18)

per1.dance()


