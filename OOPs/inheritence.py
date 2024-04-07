# inheritence : Code Reusable, Hierarchhy - Parent, child realtionship

class Animal:
    # def __init__(self, animal1):
    #     self.animal1 = animal1

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
        pass


dog = Dog()
dog.eat()

# defining inhertitence between parent and child
class Parent:
     def eat(self):
          print("All of use eat food.")

class Child(Parent):
     pass
    

child1 = Child()
child1.eat()


# Complex parent child relationship - single inheritence

class Animal:
        jungle  = "Ranthambhor"
        def __init__(self ,name):
              self.name = name

        def eat(self):
              print(f"{self.name} is playing.")

        def play(self):
              print("Animal is playing.")

class Cat(Animal):
        jungle = "Jamnagar"
        def __init__(self, name, breed):
              Animal.__init__(self, name)  # create parent instance first - parent initializer
              self.breed = breed

        def whereDoIBelong(self):
              print(f"My parent stayed in {Animal.jungle}")
              print(f"I was saved to eat laddoos at {self.jungle}")

        def play(self):
              print("Cat is playing.")

        def seeAllPlayerMethod(self):
                # parent method - we do that by super
            super().play()   # call parent method play()

        
cat = Cat("Ruby", "Raggdoll")
cat.eat()
print(f"{cat.name} and {cat.breed}")

cat.whereDoIBelong()
cat.play()  # this concept is called the method overriding

# calling parent method - play
cat.seeAllPlayerMethod()
