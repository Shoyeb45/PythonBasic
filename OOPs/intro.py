# defining class in python - class name always starts with capital letter

class Person:
    pass
    # Logic to create person object with attributes
    # Initilizer  or constructor - we use to create object
    def __init__(self, name, age):
        self.name = name
        self.age = age

per_obj = Person("Shoyeb", 19)
print(f"{per_obj.name} and {per_obj.age}")

per1 = Person("Dinkar", 60)
print(f"Age of {per1.name} is {per1.age}")


class Student:
    def __init__(self, enroId, subject, hobby):
        self.enroId = enroId
        self.subject = subject
        self.hobby = hobby

stud1 = Student(109, "Python", "Reading book")

print(f"The enrollment id is {stud1.enroId} , subject is {stud1.subject} and hobby is {stud1.hobby}")
        
# we can define only 1 init method, if we have defined multiple init method then the last method is taken into consideration.

# adding addtional attributes after defining the class

# Like I have to add attribute 'hobby' in Person class
per1.hobby = "Playing games"

print(f"Hobby of {per1.name} is {per1.hobby}")