# implicit init overloading

class Person:
    def __init__(self, name, age=99, hobby="Cricket"):
        self.name = name 
        self.age = age 
        self.hobby = hobby 

per1 = Person("Shoyeb")
per2 = Person("Shoyeb", 19)
per3 = Person("Shoyeb", 34, "Playing volleyball")

print(f"{per1.name} and {per1.age} and {per1.hobby}\n{per3.name} and {per3.age} and {per3.hobby}")