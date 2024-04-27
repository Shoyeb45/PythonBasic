# 

class Sound:
    def __init__(self):
        pass

    def makeSound(animal):
        animal.speak()

class Dog:
    def speak(self):
        print("Borf!!.... Borf!!")
class Cat:
    def speak(self):
        print("Meow... Meow.. Meow")

class Car:
    def speak(self):
        print("Horn.......")


x = Dog()
Sound.makeSound(x)
y = Cat()
Sound.makeSound(y)
z = Car()
Sound.makeSound(z)