# Binding together of data and the method
# 1) state/field -> make private
# 2) methods -> make public

# Private attribute can be created by using Two underscore(__)
# It is good practice to make all variables private
class Detail:
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
    

# Initializing with
y = Detail("D", "ds")
print(y.getCar())
y.setName("Shoyeb")
print(y.getName())
