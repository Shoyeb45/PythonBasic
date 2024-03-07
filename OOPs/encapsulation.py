# Binding together of data and the method
# 1) state/field -> make private
# 2) methods -> make public

class Person:
    # object attribute -> private
    def __init__(self, name, car):
        self.__name = name
        self.__car = car
    
    # methods -> public
        # getter Method
    def getName(self):
        return self.__name
    
        # setter Method
    def setName(self, name):
        self.__name = name

        # getter method
    def getCar(self):
        return self.__car    
        # setter Method
    def setCar(self, car):
        self.__car = car
    