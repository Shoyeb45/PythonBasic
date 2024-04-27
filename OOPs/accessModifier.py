# Two types of access modifier(in python):
# 1. Public - available to everyone
# 2. Private - Internally
# 3. Protected - Not available to outside the class, but can be accessed through the child class. (can be made by single underscore(_)) 

class Cricket:
    def __init__(self, player1, player2, fight):
        self.player1 = player1
        self.player2 = player2
        # Making private variable
        self.__fight = fight

    def play(self):
        print("I am copy crickekt champion")
        print(f"Private variable: {self.__fight}")  # we can access from the instance method because it is internal
        #  we can call private method internally
        self.__internalConvo()

    # Defining private method
    def __internalConvo(self):
        print(f"{self.player1} you just missed a stump today")

cric = Cricket("MS Dhoni", "Virat Kohli", "Rare")

print(cric.player1) # These are public variable
# print(cric.__fight)  => This will throw error :  AttributeError

cric.play()

# Accwessing private method
# cric.__internalConvo()  => It will throw error