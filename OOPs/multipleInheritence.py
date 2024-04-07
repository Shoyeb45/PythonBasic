# Diamond problem - If we have two parent method A and B, and C is child method of A and B -> C(A, B). And we have some method like play(), which is present in all the A, B and C. Then we call the method as instance of C, then in following way, the search will be followed:
# First it will search in C, and if there it is not present then it will go to that class which we have provided first in argument like C(A, B), here the search will go to the A.
# And then B.
# This method is called MRO Approach (Method Resolution Order).

# Example

class A:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("I am A.") 

class B:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("I am B.") 

class C(B, A):
    pass

    def play(self):
        print("I am in C")

class D(A, B):
    pass
    # def __init__(self, name):
    #     self.name = name

c = C("Shoyeb")
c.play()      

per1 = D("Shoyeb")
print(per1.play())

# DFS - Depth First Search 
# Internally it uses above mentioned algorithm.