class A:
    def __init__(self, name):
        self.name = name
    
    def play(self):
        print(f"{self.name} is playing")

class D:
    def sleeping():
        print(1)

class B(D):
    def sleepng():
        print(f"Sleeping....")

class C(B, A):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    
    
obj = C("F")

C.sleeping()