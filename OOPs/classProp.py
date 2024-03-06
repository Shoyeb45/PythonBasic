# defining property outside the init - class property

class Stud:
    college = "PWIOI"
    def __init__ (self, name, year):
        self.name = name 
        self.year = year 

stud1 = Stud("Mitesh", "1st year")

print(f"{stud1.name} is from {stud1.college} college and he is in {stud1.year}")